from bs4 import BeautifulSoup
from bs4 import NavigableString
import bs4
import urllib2
import sys
from Tkinter import *

a=raw_input("WELCOME TO BRAINPICKING TEXUAL MODE \nEnter URL:- ")

try:
    webpage = urllib2.urlopen(a)
    soup = bs4.BeautifulSoup(webpage.read().decode('utf8'))
except:
    print ("Cant find url")

i=0  #text i find appears twice so to print only once
m=0  # same as varible i 
a=["Heading :-","Author :-","\n"]
img=[] # to contain all the images that appears on the page 
def text(tag):
    #find the data inside the tag
    string=""
    if isinstance(tag,NavigableString)==True:
        string=tag.encode("utf-8")
        return string 
    for tags in tag.descendants:
        if isinstance(tags,NavigableString)==True:
            string=string+tags.encode("utf-8")
        elif tags.name=="img":
            return(" ")
    return string

import pprint
import time
flag=0 #for marking the end 
flag1=0 #for marking quotes 
fil="" #for storing the data 
head="" 
maindata=soup.findAll("div")
for data in maindata:
    #search for data in div tags
    if isinstance(data,NavigableString)==False:
        for atrs in data.attrs:
            if atrs=="class":
                if data['class']==['holder']:
                    i=i+1
                    if i==1:
                        continue
                    for item in data.contents:
                        string=""
                        m=m+1
                        if (m%2==1):
                            continue
                        if isinstance(item,NavigableString)==False:
                            if (item.name=="div"):
                                for atr in item.attrs:
                                    if atr=="class":
                                        if item['class']==['callout']:
                                            flag=1
                                            break
                            if (item.name=="blockquote"):
                                flag1=1
                        pp = pprint.PrettyPrinter(indent=1)

                        if flag==1:
                            break

                        if flag1==1:
                            flag1=0
                            string=string+"QUOTE:"
                            pp = pprint.PrettyPrinter(indent=4)


                        if (m<7):
                            pp = pprint.PrettyPrinter(indent=4)
                            string=string+ str(a[min(m/2-1,2)])
                        i=i+1
                        if text(item)==" ":
                            continue
                        string=string+text(item)
                        if m==2:
                            head=text(item)
                        print ((string))
                        fil=fil+string+"\n"
                        time.sleep(2 * len(string) / 50 )         
#raw_input()    
print "IMGs:"

imgs=soup.findAll("img")
for imgss in imgs :
    img.append(imgss['src'])

print img

fil = fil + "\n Download Images at :- ".encode('utf-8') + str(img).encode('utf-8')
#saving the data inside a file with the name of the heading 
fo = open(head+".txt","w") 
fo.write(fil.decode("utf-8").encode("ascii","ignore"))
fo.close
