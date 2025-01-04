#!/usr/bin/env python3 
import time
import random
import urllib 

# importing those 1000 most common words
url = "https://raw.githubusercontent.com/devildeuteragonist/word-games/refs/heads/main/guess-n-gamble/1000-common-words.txt"
with urllib.request.urlopen(url) as f: 
    words = f.read().decode("utf-8").splitlines() 

our_words = [word for word in words if len(word) > 3]

time.sleep(1)
print("Eh!??!?! Easy mode!?")
time.sleep(1)
print("How lame!")
time.sleep(1)
print("Only kids play in easy mode!")
time.sleep(1)
print("hAHAHAHAHAHA!!!")