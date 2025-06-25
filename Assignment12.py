#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Create a program that takes two strings and calculates if they are anagrams of each other. Also calculate the Hamming
distance between the strings. A hamming distance is a measure of how different two strings are from each other.

egg and pegg have a Hamming distance of 2.

You compare the strings character by character and increase Hamming distance by 1 if they are different and zero if
the same.

mead and read have a Hamming distance of 1 since the 1st characters are the only ones different.
'''

s1 = 'below'
s2 = 'elbow'
hamming = 0

for e in s1:
    if s1.count(e) != s2.count(e):
        print('They are not anagrams')
        break
else:
    print('Yes, they are anagrams')
    index = 0
    for e in s1:
        if e != s2[index]:
            hamming += 1

        index += 1
    print('The Hamming distance is:', hamming)


# In[ ]:




