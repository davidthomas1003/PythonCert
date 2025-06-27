#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
You are given two lists which have the same number of elements. Print the elements inside a single for loop.

x = [1,2,3]
y = ['one', 'two', 'three']
'''

x = [1,2,3]
y = ['one', 'two', 'three']


# In[5]:


for index, a in enumerate(x):
    print(a, y[index])


# In[6]:


print(enumerate(x))


# In[7]:


list(enumerate(x))


# In[ ]:




