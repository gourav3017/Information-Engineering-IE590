import numpy as np
from bs4 import BeautifulSoup
import urllib.request
import requests
import urllib.error
url = input("Enter a website to extract the URL's from: ")

def getlink(url):
    r  = requests.get(url)
    print(r.status_code)
    data = r.text
    soup = BeautifulSoup(data,"html5lib")
    a=[]
    for link in soup.find_all('a'):
        ax=[(link.get('href'))]
        a=a+ax
    return a

k=getlink(url)
print(k)
t=[]
for i in range(len(k)):
    try:
        urllib.request.urlopen(k[i])
        sublink=getlink(k[i])
        t=t+sublink
        print("links for:",k[i],t)
    except: urllib.error.URLError
