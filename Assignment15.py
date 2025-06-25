#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Create a program that asks the user to guess words one character at a time. The program should choose a word from a list
of words at random and ask the user to input their guesses one character at a time. If the character appears in the word,
display all the locations where the character appears and continue till the entire word has been guessed correctly. Keep 
track of the total number of tries it took to fully guess the word.
'''

word = 'hellopython'
final = ['_'] * len(word)
index = 0
guess = input('Please enter a character: ')

for e in word:
    if guess == e:
        final[index] = e
    index += 1

print(final)


# In[3]:


word = 'hellopython'
final = ['_'] * len(word)

while final != list(word):
    index = 0
    guess = input('Please enter a character: ')

    for e in word:
        if guess == e:
            final[index] = e
        index += 1
    
    print(final)


# In[ ]:




