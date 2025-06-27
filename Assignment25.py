#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Using a list comprehension, convert a list of temperatures in celsius to farenheit.
'''

x = [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100]


# In[2]:


y = [z*9/5 + 32 for z in x]
print(y, x)


# In[4]:


y = [z*9/5 + 32 for z in x if z>=0]
print(y, x)


# In[ ]:




