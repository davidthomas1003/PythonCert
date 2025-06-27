#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
You are given a list of weekday names.
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Create a new list as shown

new_weekdays = [(1,'Mon'), (2,'Tue'), (3,'Wed'), (4,'Thu'), (5,'Fri'), (6,'Sat'), (7,'Sun')]

Notice that we start with 1 rather than 0
'''

weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


# In[3]:


new_weekdays = list(enumerate(weekdays, 1))
new_weekdays


# In[ ]:




