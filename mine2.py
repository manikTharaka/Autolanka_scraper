#!/usr/bin/env python


import scraperwiki
import requests
import lxml.html
import time

ads=[]

def getText(dateString):
    s=dateString.partition(":")[2]
    s=s.strip("]")
    s=s.strip()
    return s

def getDomFromFile(url):
    #html = requests.get("http://www.autolanka.com/Buy.asp").content
    html=open('index'+str(url),'r')
    dom = lxml.html.fromstring(html.read())
    #data=minePage(dom)

    return dom

def getDomFromWeb(url):
    html = requests.get("http://www.autolanka.com/Buy.asp?ad_category_id=&search=&Page="+str(url)+"#members").content
    #html=open('index'+url,'r')
    dom = lxml.html.fromstring(html)


    return dom

raw_data=[]
data=[]
di={}


def getRawData(url):
    dom=getDomFromWeb(url)
    for entry in dom.cssselect('.BuyDataTD'):
        if len(entry) > 0:
            raw_data.append(entry[0].text_content())

def getData(last):
    for i in range(len(raw_data)):
        item=raw_data[i]
        if "Date" in item:
            sub_list=raw_data[i:i+10]
            di={
            'date_added':getText(sub_list[0]),
            'Code':getText(sub_list[1]),
            'Make':getText(sub_list[2]),
            'Model':getText(sub_list[3]),
            'Model_no':getText(sub_list[4]),
            'Year':getText(sub_list[5]),
            'Location':getText(sub_list[6]),
            'Options':getText(sub_list[7]),
            'Price':getText(sub_list[8]),
            'Additional_info':getText(sub_list[9]),

            }

            if di['Code']==last:
                print "duplicate found "+str(di['Code'])+", exiting"
                if len(data)>0:
                    return data[0]
                else:
                    return None

            scraperwiki.sql.save(unique_keys=['Code'], data=di)
            data.append(di)

    return data[0]

def writeData(dataitem):
    #    scraperwiki.sql.save_var('last_code',str(data[0]['Code']))
    #for v in data:

    scraperwiki.sql.save_var('last_code',dataitem['Code'])
    print "wrote the last code"




#################add functionality to mine data from multiple pages and to check for last saved instance

def main():
    last=getLast()
    for i in range(2):
        getRawData(i)
        first=getData(last)
        if i==0:
            if first != None:

                writeData(first)
            else:
                print "The first entry is the same as last,exiting"
                break
    #getRawData()
    #getData()
    #writeData()


def getLast():
    code=scraperwiki.sql.get_var('last_code')
    if code==None:
        code=0
    return code

if __name__=="__main__":
    main()
