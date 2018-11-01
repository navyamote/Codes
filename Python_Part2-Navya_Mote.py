# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:08:22 2018

@author: Navya
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
 
res = requests.get("https://www.top500.org/statistics/sublist/")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))[0]
df.to_csv('Python_Part2-Mote.csv', sep=',', encoding='utf-8', header=False, index=False)