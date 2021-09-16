#!/usr/bin/env python
# coding: utf-8

# # Guessing Game Challenge

# # challenge:
#     1. if a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#     2. On a player's first turn, if their guess is
#         within 10 of the number, return "WARM!"
#         further than 10 away from the number, return "COLD!"
#     3. On all subsequent turns, if a guess is
#         closer to the number than the previous guess return "WARMER!"
#         farther from the number than the previous guess, return "COLDER!"
#     4. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# 

# In[1]:


import random              ###random.randint(a,b) returns a random integer in range [a, b]

num = random.randint(1,100)


# In[2]:


print("WELCOME TO GUESS ME!")            ###Itroduction in game
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


# In[3]:


guesses = [0]           ###Create a list to store guesses


# In[ ]:





# In[4]:


#### loop that compares the player's guess to our number. If the player guesses correctly, break from the loop.
####Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN {len(guesses)} GUESSES!!')
        break
        
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




