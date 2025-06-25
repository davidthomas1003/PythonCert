#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Write a program to accept multiple comma seperated numbers AS input from the user and create a list of integers
by extracting them out of the input.
'''

x = input('Enter numbers seperated by commas: ')

my_list = x.split(',')
index = 0

for e in my_list:
    my_list[index] = int(e)
    index += 1

print(my_list)


# In[ ]:




