#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
Consider the following list which contains tuples. Each tuple has a number and a string as its elements.

x = [ (3,'Sandtino'), (1,'Vito'), (4,'Fredo'), (10,'Tessio'), (7,'Connie'), (9,'Clemenza'), (2,'Micheal')]

Sort the list in ascending order of the number
'''

x = [ (3,'Sandtino'), (1,'Vito'), (4,'Fredo'), (10,'Tessio'), (7,'Connie'), (9,'Clemenza'), (2,'Micheal')]

def sort_order(each_element):
    return each_element[0]

x.sort(key=sort_order)
x

