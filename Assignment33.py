#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
You are asked to make a Circle class with a single attribute, the radius(int or float) which is provided at construction
time. 

The class should have two methods to calculate the area and circumference of the circle.

Construct two circle objects with radius 2.6 and 10.7. Calculate the area and circumference of both.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


# In[9]:


x = Circle(2.6)
print(x.area())
print(x.circumference())


# In[10]:


x = Circle(10.7)
print(x.area())
print(x.circumference())


# In[ ]:




