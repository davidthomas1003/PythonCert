#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Consider the following tuple:
x = ('1', '2', 'hello', '23', 'python', 'abc123')

Filter the tuple to retain only the strings that have valid numbers.
'''

x = ('1', '2', 'hello', '23', 'python', 'abc123')


# In[5]:


def check(strings):
    if strings.isnumeric():
        return True
    else:
        return False


# In[6]:


y = list(filter(check, x))
print(y)


# In[ ]:




