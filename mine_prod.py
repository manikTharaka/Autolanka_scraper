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

html = requests.get("http://www.autolanka.com/Buy.asp").content
#html=open('index','r')
dom = lxml.html.fromstring(html)
#data=minePage(dom)

raw_data=[]
data=[]
di={}
def getRawData():
    for entry in dom.cssselect('.BuyDataTD'):
        if len(entry) > 0:
            raw_data.append(entry[0].text_content())

def getData():
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
            scraperwiki.sql.save(unique_keys=['Code'], data=di)
            data.append(di)

def writeData():
    for v in data:
        print str(v)+"\n"


getRawData()
getData()
writeData()
