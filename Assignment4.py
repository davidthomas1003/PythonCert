#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''Write a small script to replace the first letter of a string with its uppercase equivalent.
    The rest of the string must be untouched'''

string = input("Enter a string: ")
caps = string[0].upper() + string[1:]

print(caps)

