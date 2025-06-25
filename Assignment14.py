#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Write a program to look at all the numbers between 2 numbers and print out the ones that have only even numbers in
their digits

start = 1000
stop = 3000
'''

start = 1000
stop = 3000

for en in range(start, stop+1):
    str_en = str(en)

    for ec in str_en:
        if int(ec) % 2 != 0:
            break
    else:
        print(en)


# In[ ]:




