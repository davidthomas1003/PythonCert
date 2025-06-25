#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Reverse the list x = [1,2,3,4] using a for loop. Dont use reverse or [::-1] notation.
'''
x = [1, 2, 3, 4]

y = -1
z = [None] * len(x)

for e in x:
    z[y] = e
    y -= 1

x = z
print(x)


# In[ ]:




