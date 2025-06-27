#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
Create an employee which takes in the first and last name. Create a method that reurns the full name which is the first
plus last name seperated by a space. Also return the email address.

firstName = 'John'
lastName = 'Doe'

full name ---> 'John Doe'
email ---> 'john.doe@acme.com'

Notice that the email is all lowercase. Your full name must also have the first letters of the first and last name capitolized
whatever the capitalization of the input first and last names. Only the first letters must be capitalized.
'''

class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def full_name(self):
        return (self.firstName + ' ' + self.lastName).title()

    def email(self):
        return (self.firstName.lower() + '.' + self.lastName.lower() + '@acme.com')


# In[19]:


x = Employee('john', 'Doe')
print('Full name: ',  x.full_name(), '\nEmail: ', x.email())


# In[ ]:




