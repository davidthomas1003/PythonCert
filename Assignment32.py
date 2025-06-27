#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Create a dictionary from the two lists below. The first list should be the keys and the 2nd list should be the 
corresponding values.

x = [1, 2, 3, 4]
y = ['one', 'two', 'three', 'four']
'''

x = [1, 2, 3, 4]
y = ['one', 'two', 'three', 'four']


# In[2]:


z = zip(x, y)
my_dict = dict(z)
my_dict


# In[ ]:




