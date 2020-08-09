#!/usr/bin/env python
# coding: utf-8

# In[101]:


from bs4 import BeautifulSoup as bs
import requests


# In[102]:


link="https://news.ycombinator.com"


# In[103]:


page=requests.get(link)


# In[24]:


soup=bs(page.content,'html.parser')


# In[27]:


print(soup.prettify())


# In[35]:


names=soup.find_all('td',class_='votelinks')


# In[49]:


titles=soup.find_all('a',class_='storylink')
title_list=[]
for i in range(0,len(titles)):
    title_list.append(titles[i].get_text())

           


# In[104]:


title_list


# In[105]:


score=soup.find_all('span',class_='score')
score_list=[]
for i in range(0,len(score)):
    score_list.append(score[i].get_text())


# In[65]:


score_list


# In[66]:


url=soup.find_all('span',class_='sitestr')
url_list=[]
for i in range(0,len(url)):
    url_list.append(url[i].get_text())


# In[106]:


url_list


# In[107]:


import pymongo
from pymongo import MongoClient
try:
    cluster =MongoClient("mongodb+srv://jyoti:1234@cluster0.nb8bu.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster["test"]
    collection=db["test"]
    print("Connected")
except:
    print("Not connected")


# In[108]:


l2=len(url_list)
for i in range(0,l2):
    temp={"Title":title_list[i],"URL":url_list[i],"Score":score_list[i]}
    collection.insert_one(temp)


# In[ ]:




