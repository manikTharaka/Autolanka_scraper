
In [1]: 
In [2]: 
In [5]:   File "/tmp/ipython-2357LWX.py", line 73
    if __name__=="__main__";
                           ^
SyntaxError: invalid syntax


In [6]: wrote the last code

In [7]: 125771

In [8]: ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-8-3f170e6bc70c> in <module>()
----> 1 execfile(r'/tmp/ipython-2357y0p.py') # PYTHON-MODE

/tmp/ipython-2357y0p.py in <module>()

/tmp/ipython-2357y0p.py in main()

/tmp/ipython-2357y0p.py in getRawData(url)

/tmp/ipython-2357y0p.py in getDomFromFile(url)

TypeError: cannot concatenate 'str' and 'int' objects

In [9]: duplicate found, exiting
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-9-ffe3af3e00ca> in <module>()
----> 1 execfile(r'/tmp/ipython-2357_-v.py') # PYTHON-MODE

/tmp/ipython-2357_-v.py in <module>()
    100 
    101 if __name__=="__main__":
--> 102     main()

/tmp/ipython-2357_-v.py in main()
     85     for i in range(2):
     86         getRawData(i)
---> 87         first=getData(last)
     88         if i==0:
     89             writeData(first)

/tmp/ipython-2357_-v.py in getData(last)
     65             if di['Code']==last:
     66                 print "duplicate found, exiting"
---> 67                 return data[0]
     68 
     69             scraperwiki.sql.save(unique_keys=['Code'], data=di)

IndexError: list index out of range

In [10]: duplicate found, exiting
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-10-d167503eb76c> in <module>()
----> 1 execfile(r'/tmp/ipython-2357MJ2.py') # PYTHON-MODE

/tmp/ipython-2357MJ2.py in <module>()
    103 
    104 if __name__=="__main__":
--> 105     main()

/tmp/ipython-2357MJ2.py in main()
     90         first=getData(last)
     91         if i==0:
---> 92             writeData(first)
     93     #getRawData()

     94     #getData()


/tmp/ipython-2357MJ2.py in writeData(dataitem)
     78     #    scraperwiki.sql.save_var('last_code',str(data[0]['Code']))

     79     #for v in data:

---> 80     scraperwiki.sql.save_var('last_code',str(dataitem['Code']))
     81     print "wrote the last code"
     82 

TypeError: string indices must be integers

In [11]: duplicate found, exiting
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-11-0ce1d46a266d> in <module>()
----> 1 execfile(r'/tmp/ipython-2357-SF.py') # PYTHON-MODE

/tmp/ipython-2357-SF.py in <module>()
    103 
    104 if __name__=="__main__":
--> 105     main()

/tmp/ipython-2357-SF.py in main()
     90         first=getData(last)
     91         if i==0:
---> 92             writeData(first)
     93     #getRawData()

     94     #getData()


/tmp/ipython-2357-SF.py in writeData(dataitem)
     78     #    scraperwiki.sql.save_var('last_code',str(data[0]['Code']))

     79     #for v in data:

---> 80     scraperwiki.sql.save_var('last_code',dataitem['Code'])
     81     print "wrote the last code"
     82 

TypeError: string indices must be integers

In [12]: duplicate found, exiting
It's the same code as the last item
---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-12-d09dadd1e8bd> in <module>()
----> 1 execfile(r'/tmp/ipython-2357LdL.py') # PYTHON-MODE

/tmp/ipython-2357LdL.py in <module>()
    106 
    107 if __name__=="__main__":
--> 108     main()

/tmp/ipython-2357LdL.py in main()
     90     last=getLast()
     91     for i in range(2):
---> 92         getRawData(i)
     93         first=getData(last)
     94         if i==0:

/tmp/ipython-2357LdL.py in getRawData(url)
     39 
     40 def getRawData(url):
---> 41     dom=getDomFromFile(url)
     42     for entry in dom.cssselect('.BuyDataTD'):
     43         if len(entry) > 0:

/tmp/ipython-2357LdL.py in getDomFromFile(url)
     19 def getDomFromFile(url):
     20     #html = requests.get("http://www.autolanka.com/Buy.asp").content

---> 21     html=open('index'+str(url),'r')
     22     dom = lxml.html.fromstring(html.read())
     23     #data=minePage(dom)


IOError: [Errno 2] No such file or directory: 'index1'

In [13]: duplicate found, exiting
It's the same code as the last item
duplicate found, exiting

In [14]: wrote the last code

In [15]: duplicate found, exiting
i is 0
It's the same code as the last item
duplicate found, exiting

In [16]: duplicate found 125771, exiting
i is 0
It's the same code as the last item
duplicate found 125771, exiting

In [17]:   File "/tmp/ipython-2357MQq.py", line 85
    break
SyntaxError: 'break' outside loop


In [18]: duplicate found 125771, exiting
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-18-05c1ea45774d> in <module>()
----> 1 execfile(r'/tmp/ipython-2357Zaw.py') # PYTHON-MODE

/tmp/ipython-2357Zaw.py in <module>()
    111 
    112 if __name__=="__main__":
--> 113     main()

/tmp/ipython-2357Zaw.py in main()
     93         first=getData(last)
     94         if i==0:
---> 95             if first != none:
     96                 print "i is "+str(i)
     97                 writeData(first)

NameError: global name 'none' is not defined

In [19]: duplicate found 125771, exiting
The first entry is the same as last,exiting

In [20]: ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/home/bushcat/dev/RESEARCH/Autolanka/<ipython-input-20-afe44590f450> in <module>()
----> 1 execfile(r'/tmp/ipython-2357YuF.py') # PYTHON-MODE

/tmp/ipython-2357YuF.py in <module>()
    111 
    112 if __name__=="__main__":
--> 113     main()

/tmp/ipython-2357YuF.py in main()
     90     last=getLast()
     91     for i in range(2):
---> 92         getRawData(i)
     93         first=getData(last)
     94         if i==0:

/tmp/ipython-2357YuF.py in getRawData(url)
     39 
     40 def getRawData(url):
---> 41     dom=getDomFromWeb(url)
     42     for entry in dom.cssselect('.BuyDataTD'):
     43         if len(entry) > 0:

/tmp/ipython-2357YuF.py in getDomFromWeb(url)
     26 
     27 def getDomFromWeb(url):
---> 28     html = requests.get("http://www.autolanka.com/Buy.asp?ad_category_id=&search=&Page="+url+"#members").content
     29     #html=open('index'+url,'r')

     30     dom = lxml.html.fromstring(html)

TypeError: cannot concatenate 'str' and 'int' objects

In [21]: i is 0
wrote the last code

In [22]: 