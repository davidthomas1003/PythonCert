#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Writer a list of comprehension which doubles the +ve numbers in a list and halves the -ve numbers.
c = [1,2,-3,-4,5,-6,7]
'''

c = [1,2,-3,-4,5,-6,7]


# In[2]:


x = [y*2 if y>=0 else y/2 for y in c]
print(x, c)


# In[ ]:




