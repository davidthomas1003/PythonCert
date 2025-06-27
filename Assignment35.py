#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
You are asked to create a Car class and then three Car objects with certain instance attributes. However, the instance attribute
names and values are provided to you as a dictionary of key-value pairs where the key is the attribute name and the corresponding
value is the value of the attribute. For example:

car1_attr = {"year": 1990, "make":"Ford", "model":"Bronco"}
car2_attr = {"year": 2010, "make":"Chevy", "model":"Blazer", "drive":"RWD"}
car3_attr = {"year": 2020, "make":"Tesla", "model":"Model3", "drive":"AWD", "range": 300}

Create a generic dunder init method that will accept the dictionaries above and create the instance attributes. Your solution must
be able to accomodate any future attributes which can be different than the ones above.
'''

car1_attr = {"year": 1990, "make":"Ford", "model":"Bronco"}
car2_attr = {"year": 2010, "make":"Chevy", "model":"Blazer", "drive":"RWD"}
car3_attr = {"year": 2020, "make":"Tesla", "model":"Model3", "drive":"AWD", "range": 300}


# In[2]:


class Car:
    def __init__(self, attr_dict):
        for x, y in attr_dict.items():
            setattr(self, x, y)


# In[3]:


car1 = Car(car1_attr)
car1.__dict__


# In[4]:


car2 = Car(car2_attr)
car2.__dict__


# In[5]:


car3 = Car(car3_attr)
car3.__dict__


# In[ ]:




