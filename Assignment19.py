#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Write a function that takes 3 parameters the birth year of a man, woman and their child and calculates the ages of the father 
and mother when the child was born.

Perform some checking to see that the birth year of the father and mother are at least 18 years when the child was born but the
age of the either parent cannot be greater than 60 when the child was born.

Output the appropriate message when the ages are out of these bounds.
'''

def ages(father, mother, child):
    age_father = child - father
    age_mother = child - mother
    if age_father < 18 or age_mother < 18:
        print('Parents age is to low')
    elif age_father > 60 or age_mother > 60:
        print('Parents age is to high')
    else:
        print('Fathers age: ', age_father)
        print('Mothers age: ', age_mother)


# In[2]:


ages(1940, 1952, 2015)


# In[3]:


ages(1961, 1975, 2012)


# In[ ]:




