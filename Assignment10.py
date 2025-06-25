#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
A weight lifter bench presses every day and keeps track of the weights inside a list on a day to day basis. He wants to 
measure his progress and has what he calls a progress day. This is a day where he has lifted more weight on a particular
day then the two days preceeding.
For example
[200, 205, 210, 206]
The 3rd day would be considered a progress day because 210 is larger than 200 and 205 (the two preceeding weights). However,
the 4th day is not because while 206 is greater than 205, it is not greater than 210. Equality of weights does not count as 
a progress day. [180, 190, 190, 191]. The 3rd day is not a progress day while the 4th day is.
'''

weights = [180, 190, 190, 191]

progress = 0

for x in range(2, len(weights)):
    if (weights[x] > weights[x-1]) and (weights[x] > weights[x-2]):
        progress += 1

print(progress)


# In[ ]:




