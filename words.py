# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:52:13 2018

@author: Navya
"""

print("Hello World!")
#%%
import pandas as pd
num = pd.read_csv('C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 6/num.csv')  
df = num.sort_values('num')     
print(df)
#%%
count=[]
num=[]
file = open("C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 6/words.txt", "r")
from collections import Counter
wordcount = Counter(file.read().split())
for item in wordcount.items(): print("{}\t{}".format(*item))
count = sum(wordcount.itervalues())
print("No. of words :", count)
num = len(wordcount)
print("No. of distinct words :", num)
#%%
df.plot.hist(alpha=0.5)
#%%
import pandas as pd
tweet = pd.read_csv('C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 6/Hashtags.csv')  
hashtags = tweet.Hashtags.str.findall(r'#.*?(?=\s|$)')
print(hashtags)
f_hashtags = hashtags[hashtags.apply(len) > 0]                              