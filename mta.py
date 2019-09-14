# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:24:14 2019

@author: Reshikesh
"""

import requests
from bs4 import BeautifulSoup 
import re
from urllib.request import urlopen
import sqlite3
import pandas as pd


#Run this par tonly once Then comment it ------>
# =============================================================================
# url='http://web.mta.info/developers/turnstile.html'
# page=requests.get(url)
# b=[]
# soup=BeautifulSoup(page.content,"html.parser")
# a=soup.find_all(class_="span-84 last")
# for link in soup.findAll('a', attrs={'href': re.compile("txt$")}):
#     b.append(link.get('href'))
#     print(b)
# n=len(b)
# url1=f'http://web.mta.info/developers/{a}'
# for i in b:
#     
#     name=i[-10:-4]
#     url1=f'http://web.mta.info/developers/{i}'
#     data=urlopen(url1).read().decode('utf-8')
#     for j in range(n):
#         fileobj= open(f'{j}.csv','w')
#         fileobj.write(data)
# 
# =============================================================================
#-------------------------->
conn= sqlite3.connect('mt.db')
for i in range(484):
    df=pd.read_csv(f'{i}.csv',error_bad_lines=False)
    df.to_sql(name=f'file{i}',con=conn)
con.commit()
con.close()


