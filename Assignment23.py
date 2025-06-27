#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Create a function that will count the number of uppercase and lowercase characters in a string.
'''

def count(x):
    lower_case = 0
    upper_case = 0
    for y in x:
        if y.isupper(): upper_case += 1
        elif y.islower(): lower_case += 1
    return upper_case, lower_case


# In[3]:


count('How many letters is this sentence?')


# In[4]:


count('How About This Sentence?')


# In[ ]:




