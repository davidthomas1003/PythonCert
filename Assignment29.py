#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
Use a map function to convert the following list of weekday names to their short forms i.e. first three letters. Ensure
that the first letter is capitalized.

weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
'''

weekdays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']


# In[9]:


def short(weekday):
    x = weekday[0:3]
    y = x.capitalize()
    return y


# In[10]:


first_weekday = list(map(short, weekdays))
print(first_weekday)


# In[ ]:




