#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
In the game of poker, the player holds 2 cards in his hand and there are 5 cards on the table. You have a flush IF
out of these 7 cards, 5 of them come from a single suit i.e. spades, diamonds, hearts and clubs. Given two lists, one
for the table and one for the hand, write a snippet of code to determine if you have a fluch or not. Each card is 
represented by a number (1, 2, 3, 10, J, Q, K) followed by a hyphen and then the 1 letter suit abbreviation. So
J-H is Jack of Hearts and A-S is the ace of spades.
'''


# In[2]:


table = ['A-S', '10-S', '2-D', '3-H', '7-S']
hand = ['3-S', '5-S']

table_suits = ''
hand_suits = ''


# In[3]:


for e in table:
    suit = e.split('-')[1]
    table_suits += suit

for e in hand: 
    suit = e.split('-')[1]
    hand_suits += suit

all_suits = table_suits + hand_suits


# In[4]:


count = {}
count['H'] = all_suits.count('H')
count['S'] = all_suits.count('S')
count['D'] = all_suits.count('D')
count['C'] = all_suits.count('C')


# In[5]:


for s, c in count.items():
    if c >= 5:
        print(f'You have a flush of {c} cards in {s}')
        break
else:
    print('You have no flushes')


# In[ ]:




