#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

from bs4 import BeautifulSoup
 
import requests


html=open('index','r')
print html.read()
soup = BeautifulSoup(html)
print(soup.pretify)
