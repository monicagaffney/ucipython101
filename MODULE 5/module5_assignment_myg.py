#!/usr/bin/env python
# coding: utf-8

# # Module Five Homework for Prof. Henry

# # Problem  1:  
# Create the following variable, my_word_list = [‘apple’, ‘orange’, ‘banana’]. Then, use the map function (and lambda keyword) to produce the list [‘_apple’ ,’_orange’, ’_banana’]. Assign the list to the variable, my_new_word_list, and print it.

# In[19]:


my_word_list = ['apple', 'orange', 'banana']
map_results = map(lambda x: '_' + x,my_word_list)
for my_new_word_list in map_results:
    print(my_new_word_list)


# # Problem 2:
# Create the following variable, my_state_list = [‘CA’, ‘OR’, ‘NY’, 'OR’]. Use the filter and lambda keyword to produce the list [‘CA’, ‘NY’]. Assign this list to the variable my_new_state_list, and print it.

# In[52]:


my_state_list = ['CA', 'OR', 'NY', 'OR']
my_new_state_list = filter(lambda x: x in ['CA', 'NY'], my_state_list) 


# In[53]:


print(list(my_new_state_list))


# # Problem 3:
# Create the following variable, my_number_list = [1, 2, 3, 4, 5]. Use a list comprehension to multiply each number by 3, and produce the list [3, 6, 9, 12, 15]. Assign this to the variable, my_new_number_list, and print it. 

# In[60]:


my_number_list = [1, 2, 3, 4, 5]
my_new_number_list = map(lambda x: (x * 3), my_number_list)
print(list(my_new_number_list))


# # Problem 4:
# Create the following two lists, list_of_words = [‘love’, ‘the’, ‘outdoors’, ‘with’ , ’passion’], and words_to_temove = [‘the’, ‘with’, ‘of’, ‘a’]. Then create a new list that only contains the words in list_of_words that are not in wordsToRemove. Do this with a list comprehension. You will have an ‘if’ statement in your list comprehension. We did something similar in the lectures. 

# In[69]:


list_of_words = ['love', 'the', 'outdoors', 'with' , 'passion', 'a']
words_to_remove = ['the', 'with', 'of', 'a']

listCompResults_1 = [x for x in list_of_words if x in ['love', 'outdoors', 'passion']]
print(listCompResults_1)

listCompResults_2 = [x for x in words_to_remove if x in ['the', 'with', 'of', 'a']]
print(listCompResults_2)


# # Problem 5:
# Repeat problem 4, except this time accomplish it using the filter function, instead of using a list comprehension.b

# In[67]:


list_of_words = ['love', 'the', 'outdoors', 'with' , 'passion', 'a']
filterResults = filter(lambda x: x in  ['love', 'outdoors', 'passion'], list_of_words)
print(list(filterResults))

