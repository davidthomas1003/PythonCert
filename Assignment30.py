#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Consider the following tuple with a bunch of floating point numbers. Write a map function which returns a list subject
to the following conditions

If a number is less than -1, then we replace it with a zero.
If a number is greater than 1, then we replace it was a one.
If a number is between -1 and +1, we round it to 1 decimal point.

org = (-1.5, -0.756, 0.91, 5.6, -10.0, 12,2)
'''

org = (-1.5, -0.756, 0.91, 5.6, -10.0, 12,2)


# In[5]:


def relu(number):
    if number < -1:
        number = 0
    elif number > 1:
        number = 1
    else:
        number = round(number, 1)
    return number


# In[7]:


my_list = list(map(relu, org))
print(my_list)


# In[ ]:




