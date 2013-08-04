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
                val=word[index]
                index =index+1
        else:
            val="NULL"

        if val == None:
            return

        if var=="Added:":
            var="Date Added:"
        if var=="No:":
            var="Model No:"

        di[var]=val
        return val



#html = requests.get("http://www.autolanka.com/Buy.asp").content
html=open('index','r')
dom = lxml.html.fromstring(html.read())


varia=["Code:","Added:","Make:","Model:","No:","Year:","Location:","Options:","Price:","Info:"]
di={}
ads={}

for entry in dom.cssselect('.BuyDataTD'):
    [extract(var,entry,di) for var in varia]
    if len(di)==10 and di['Code:'] not in ads.keys():
        ads[di['Code:']]=di
        print di['Code:']+" ok"
