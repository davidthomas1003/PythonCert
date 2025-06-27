#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Write a function that will take a list of numbers and return the maximum value of that list. Do not use the max function.
'''

def max_list(my_list):
    my_max = float('-inf')
    for x in my_list:
        if x > my_max:
            my_max = x
    return my_max


# In[4]:


max_list([-20, -10, 0, 10, 20])


# In[ ]:




