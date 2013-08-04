#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html
import time


def extract(var,entry,di):
    if var in entry.text_content():
        word=entry.text_content().split()
        index=word.index(var)+1
        if len(word) > index:
            while len(word) > index:
                val=var+word[index]
                index =index+1
        else:
            val=var+"NULL"
            
        #print var+val+"\n"
        if val == None:
            return
        di[var]=val
        return val

#html = requests.get("http://www.autolanka.com/Buy.asp").content
html=open('index','r')
dom = lxml.html.fromstring(html.read())


varia=["Code:","Added:","Make:","Model:","No:","Year:","Location:","Options:","Price:","Info:"]
di={}
ads={}
for entry in dom.cssselect('.BuyDataTD'):
    [extract(val,entry,di) for val in varia]
    if (len(di)==10) and not(di['Code:'].replace("Code:","") in ads):
        ads[di['Code:'].replace("Code:","")]=di
    print ads
    print"\n"    
    
    
 


    

