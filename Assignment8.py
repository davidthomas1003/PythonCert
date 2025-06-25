#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Write code so that given a string with an odd number of characters and greater than 7 characters, return the middle
5 characters.
'''

x = input("Enter a string: ")
y = int((len(x) - 1) / 2)
z = x[y - 2: y + 3]
print(z)


# In[ ]:




