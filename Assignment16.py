#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Tax Tables:
A country has the following income tax structure:
0-10000 0%
10001-20000 5% above 10000
20001-50000 10% above 20000 plus
50001-100000 15%
100001 and above 20%

The tax structure is progressive i.e. if a persons income is $25,000, the first 10000 incurs 0% income tax, the next
$9,999 a 5% tax and the remaining $4,999 at 10%. The total tax owed is then: 

10,000 * 0 + (20,000 - 10,000) * .05 + (25,000 - 20,000) * .1 = 10000
'''

tax_range = [
    (0, 10000, 0),
    (10001, 20000, 0.05),
    (20001, 50000, 0.1),
    (50001, 100000, 0.15),
    (100001, float('inf'), 0.2)
]


# In[2]:


income = 203000
tax = 0

for each in tax_range:
    if income > each[1]:
        tax = tax + (each[1] - each[0]) * each[2]
    else:
        tax = tax + (income - each[0]) * each[2]
        break
print(tax)

