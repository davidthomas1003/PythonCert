#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Write a map-reduce to calculate the square root of the sum of squares of a list of integers.
'''

x = [1, 2, 3]

from functools import reduce

distance = reduce(lambda e1, e2: (e1**2+e2**2)**0.5, x)
print(distance)


# In[ ]:




