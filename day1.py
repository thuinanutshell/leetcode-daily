#!/usr/bin/env python
# coding: utf-8

# ### Pseudocode
# - Start with the middle index of the list as the initial guess
# - If the guess is less than the actual number, choose the middle index of the left half of the list
# - If the guess is greater than the actual number, choose the middle index of the right half of the list
# - Continue until the guess is correct

# ### Implementation

# In[1]:


import numpy as np


# In[2]:


np.random.choice([1, 2, 3])


# In[27]:


2%2


# In[28]:


def binary_search(lst):
    answer = np.random.choice(lst)
    print("Number you have to guess is:", answer)
    
    sorted_list = sorted(lst)
    print("Sorted list:", sorted_list)
    
    if len(lst) % 2 == 0:
        mid_idx = len(sorted_list) // 2 + 1
    else:
        mid_idx = len(sorted_list) // 2
    print("The middle index:", mid_idx)
    
    start_idx, end_idx = 0, len(lst)-1
    print("Start index & End index:", start_idx, end_idx)
    
    guess = sorted_list[mid_idx]
    print("Guess:", guess)
    
    while guess != answer and start_idx < end_idx and len(sorted_list[start_idx:end_idx]) >= 2:
        
        if guess < answer:
            print("Guess is smaller than answer:", guess < answer)
            
            start_idx, end_idx = mid_idx, end_idx
            print("Start index & End index:", start_idx, end_idx)
            n1 = len(sorted_list[start_idx:end_idx]) 
            
            mid_idx = n1//2 + mid_idx
            print("Mid index:", mid_idx)
            
            guess = sorted_list[mid_idx]
            print("Update guess:", guess)
        
        elif guess > answer:
            print("Guess is greater than answer:", guess > answer)
            
            start_idx, end_idx = start_idx, mid_idx
            print("Start index & End index:", start_idx, end_idx)
            
            mid_idx = len(sorted_list[start_idx:end_idx])//2 + start_idx
            print("Mid index:", mid_idx)
            
            guess = sorted_list[mid_idx]
            print("Updated Guess:", guess)
        
        else:
            guess = guess
            print(guess)
    return guess


# In[29]:


lst = [0, 5, 6, 7, 4, 9, 10]


# In[38]:


binary_search(lst)

