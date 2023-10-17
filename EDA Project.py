#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[ ]:





# In[2]:


# import Gaming dataset 
data = '/Users/hambolu/Downloads/Video_Games_Sales_as_at_22_Dec_2016.csv'
df = pd.read_csv(data)
df.head()


# In[3]:


#Gaming dataset frequency distributions 
plt.hist(df['Global_Sales'], bins=25)
plt.xlabel('Global Sales')


# In[4]:


#Frequency distributions of 
df.hist(bins = 50, figsize=(20,15))


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.nunique()


# In[8]:


df.isna().any()


# In[9]:


sns.heatmap(df.isnull())


# In[ ]:





# In[10]:


df.isnull()


# In[11]:


# Most popular gaming publishers
Publisher = df['Publisher'].value_counts().sort_values(ascending = False)
print(Publisher)


# In[12]:


#Top 3 publihsers grouped 
top_3 = df.nlargest(20, 'Global_Sales')
sns.barplot(data = top_3, x = "Publisher", y = "Global_Sales")


# In[13]:


sns.barplot(data = df, x = "Publisher", y = "Global_Sales")


# In[14]:


#top critic scores by genre
Critic = df.nlargest(20, 'Critic_Score')
C1 = sns.barplot(data = Critic, x = 'Critic_Score', y = "Genre")
for i in C1.containers:
    C1.bar_label(i,)


# In[15]:


# Checking for correlation by unstacking data
corr = df.corr()
c1 = corr.abs().unstack()
c1.sort_values(ascending = False)


# In[16]:


#Correlation between columns
plt.figure
sns.heatmap(df.corr(), annot=True)


# In[17]:


#Most popular year for games releases 
variety = df['Year_of_Release'].value_counts(ascending = False)
print(variety)


# In[18]:


#Top 3 major sales by platform
Biggest_platform = df.nlargest(5, 'Global_Sales')
sns.barplot(data = Biggest_platform, x = 'Global_Sales', y = 'Platform', color = 'purple')


# In[19]:


#Top 5 major sales by genre
Largest_genre = df.nlargest(6, 'Global_Sales')
sns.barplot(data = Largest_genre, x = 'Global_Sales', y = 'Genre')


# In[20]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




