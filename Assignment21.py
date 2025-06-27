#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Write a function that swaps the keys and values of a dictionary. Assume the values are immutable.
'''

def swap(my_dict):
    swapped_dict = {}
    for k, v in my_dict.items():
        swapped_dict[v] = k
    return swapped_dict


# In[4]:


x = {1:'one', 2:'two', 3:'three'}
swap(x)


# In[ ]:




