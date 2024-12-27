#!/usr/bin/env python3

# importing those 1000 most common words
with open('1000-common-words.txt', 'r') as f: 
    words = f.read().splitlines() 

# (importing something for a magic trick)
import time

# cleaning the file of words three letters or shorter 
our_words = [word for word in words if len(word) > 4]
    # there are brackets here so python knows we are dealing with 
    # a list. this is so we don't have to use a for loop because 
    # we are cute and smart like that. 

# (fun easter eggs) 
egg_1 = "A machine must behave like a machine" 

# computer chooses a word  
import random 
puter_word = random.choice(our_words)

# the game will last multiple rounds, so the machine has to know that. 
total_rounds = 5
def round_number(total_rounds, puter_word, egg_1):
    round_number = 1

    while round_number <= total_rounds:
        print(f"Get ready for round {round_number}!")

        # computer prompts YOU to guess what it's saying 
        print("Ya think you can play against me?")
        time.sleep(1)
        print("...")
        time.sleep(0.5)
        print(f"I'm thinking of a word that is {len(puter_word)} letters long...")
        print(f"...that starts with {puter_word[0]}.")
        guessing = input("Enter your guess: ")
        print(guessing)

        # return whether guess was correct or incorrect
        if guessing == puter_word: 
            print("Ugh. Can't believe you managed to get me this early...")
        elif guessing == egg_1:
            print("W-What?! Who taught you that saying?! I am aborting this game immediately!") 
            time.sleep(1)
            print("Aborting...") 
            time.sleep(2)
            print("GAME OVER") 
        else: 
            print("Ha! Try again.")
            if len(puter_word) > 6:
                print(f"The word starts with these two letters: {puter_word[0:2]}")
                print(f"The word also ends with this letter: {puter_word[-1]}")
                guessing2 = input("Enter your guess: ")
                print(guessing2)
                if guessing2 == puter_word: 
                    print("Man. I guess you got it.")
                else: 
                    print(f"The word also contains this letter: {puter_word[3]}")
                    guessing4 = input("Enter your guess: ")
                    print(guessing4)
                    if guessing4 == puter_word: 
                        print("Drat! How could you beat me!?")
                    else: 
                        print(f"This round of the game is over. The word was '{puter_word}'.")
                        time.sleep(1)
                        print("I win, you lose. Loser.")
            if len(puter_word) <= 6: 
                print(f"The word also ends with this letter: {puter_word[-1]}")
                guessing3 = input("Enter your guess: ")
                print(guessing3)
                if guessing3 == puter_word: 
                    print("You win this round...")
                    time.sleep(2)
                    print("BUT I'LL GET YOU NEXT TIME!")
                else:
                    print(f"The word also contains this letter: {puter_word[2]}")
                    guessing5 = input("Enter your guess: ")
                    print(guessing5)
                    if guessing5 == puter_word:
                        print("You got me beat...")
                        time.sleep(2)
                        print("BUT THAT WON'T HAPPEN AGAIN!")
                    else:
                        print(f"The round for this game is over. The word was '{puter_word}'.")
                        time.sleep(1)
                        print("It's men versus machines, baby! And I WON!")
        round_number += 1
    print("GAME OVER! Let's see what we got...")
# note to self: it's not fair yet, but it's cooking. 
# might add easter eggs, like i want it to be offended if you can push its buttons 
# in particular ways. 
# another note to self: maybe make the third hint random. 
