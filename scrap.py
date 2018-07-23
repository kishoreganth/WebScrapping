# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:47:38 2018

@author: kisho
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd 


site= "http://trak.in/india-startup-funding-investment-2015/january-2017/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup)


# reading the table 

table = soup.table  
print(table)


table_rows = table.find_all('tr')
print(table_rows)
data = []   


for i in range(len(table_rows)):
    row = []
    for td in table_rows[i].find_all('td'):
        row.append(td.getText())
    data.append(row)
    
    
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
    data.append(row)
    
    
    
dfs = pd.read_html('http://trak.in/india-startup-funding-investment-2015/january-2017/')
for df in dfs:
    print(df)

# #    PANDAS     
import requests
url = 'http://trak.in/india-startup-funding-investment-2015/january-2017/'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
r = requests.get(url, headers=header)
dfs = pd.read_html(r.text)