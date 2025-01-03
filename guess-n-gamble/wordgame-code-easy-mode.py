#!/usr/bin/env python3 
import time
import random

# importing those 1000 most common words
with open('1000-common-words.txt', 'r') as f: 
    words = f.read().splitlines() 

our_words = [word for word in words if len(word) > 3]

time.sleep(1)
print("Eh!??!?! Easy mode!?")
time.sleep(1)
print("How lame!")
time.sleep(1)
print("Only kids play in easy mode!")
time.sleep(1)
print("hAHAHAHAHAHA!!!")