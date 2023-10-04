#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("C:\Users\GEEK\Documents\salary.py")
data2 = pd.read_csv("C:\Users\GEEK\Documents\salary.py/Partially Cleaned Salary Dataset.csv")


# In[5]:


data.head()


# In[6]:


data2.head()


# In[7]:


data.info()


# In[8]:


data2.info()


# In[9]:


data.describe()


# In[10]:


data2.describe()


# In[11]:


data.duplicated().sum()


# In[12]:


data2.duplicated().sum()


# In[16]:


data.isna().sum()


# In[14]:


data2.isna().sum()


# In[19]:


new_data = data.dropna(axis = 0, how ='any') 


# In[20]:


new_data.isna().sum()


# In[26]:


data3=pd.merge(new_data, data2,on='Company Name')


# In[28]:


data3.head()


# In[30]:


from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split( data3, test_size=0.25)
train_data


# In[32]:


data3.boxplot('Salaries Reported_x')


# In[34]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15, 5))
sns.barplot(x=data3['Job Title_x'], y=data3['Salary_y'])
plt.xticks(rotation='90')


# In[ ]:




