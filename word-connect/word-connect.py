#!/usr/bin/env python3

# importing necessary packages
import random 
import time

# importing our library of words into our file. 
with open('5000-common-words.txt','r') as f:
     words = f.read().splitlines()

# set quantities for number of rounds
round_count = 1
total_rounds = 149

while round_count <= total_rounds:
      print("Welcome to Word Connect!") 
      time.sleep(0.5)
      print("...") 
      time.sleep(0.25)
      print("I'm Ace, and I'm delighted to play this game with you.")
      time.sleep(0.5)


# work in progress. this code won't work now but i need to sleep. 
# i want to make it so that the player wins if they do not type in
# 'i give up' before the number of rounds is over. 
# Ace is the opposite of Adrian, the other robot from the other wordgame in 
# this repo so far. 
