#!/usr/bin/env python3

# importing those 5000 most common words
with open('5000-common-words.txt', 'r') as f: 
    words = f.read().splitlines() 

# (importing something for a magic trick)
import time

# cleaning the file of words three letters or shorter 
our_words = [word for word in words if len(word) > 4 and len(word) < 10]
    # there are brackets here so python knows we are dealing with 
    # a list. this is so we don't have to use a for loop because 
    # we are cute and smart like that. 
 
# let's give our computer some...personality. 
robot_rizz = ["Ya think you can play against me?", "My riddles will twist your squishy flesh-brain into a pretzel!",
    "You've decided to be my opponent? How daring.", "You're naive enough to think you can beat me. It sure shows, kid.",
    "Kahahaha! Beating you will be fun."]

# set the starting number of points for both human and machine
machine = 0 
human = 0          

# set quantities for number of rounds
round_count = 1      
total_rounds = 20

# instructions yes or no
instruction = input("(This is the programmer speaking.\nDo you need instructions for The Guessing Game?) y/n: ")
while instruction not in ["y", "n"]:
    instruction = input("Please enter y or n, lowercase with no spaces or punctuation: ")
if instruction == "y":
    print("(You are given 15 seconds to read the following instructions\nbefore the game starts:)")
    time.sleep(1)
    print("===================================================================================")
    print("(This game is best played with a pencil and paper in hand.\nPlease do not look up any words. That is cheating!)")
    print("(Input is case-sensitive, and sensitive to spaces and other characters.\nThe computer is also extremely obnoxious.)")
    print("===================================================================================")
    time.sleep(15)
elif instruction == "n": 
    print("(Okay. Good luck!)")

# game
while round_count <= total_rounds:
    # computer chooses a word  
    import random 
    puter_word = random.choice(our_words) 

    # round/point counter for the reference of the player
    time.sleep(2)
    print(f"ROUND {round_count} OF 20 STARTS")
    time.sleep(0.5)
    print(f"player {human} points, computer {machine} points")      
    
    # computer prompts YOU to guess what it's saying 
    print(random.choice(robot_rizz))
    time.sleep(1)
    print("...")
    time.sleep(0.5)
    print(f"I'm thinking of a word that is {len(puter_word)} letters long...")
    print(f"...that starts with {puter_word[0]} and ends with {puter_word[-1]}.")
    time.sleep(0.5)
    # offer hint if the word is long 
    if len(puter_word) > 6:
        query = input("Want an extra hint this round for 0.5 points? y/n: ")
        while query not in ["y", "n"]:
            query = input("Please enter y or n, lowercase with no spaces or punctuation: ")
        if query == "y":
            human -= 0.5
        elif query == "n": 
            human += 0
        time.sleep(0.25)
        print("...")
        time.sleep(0.5)
    guessing = input("Enter your guess: ")

    # return whether guess was correct or incorrect
    if guessing == puter_word: 
        print("Ugh. Can't believe you managed to get me this early...")
        human += 2 
    else: 
        print("Ha! Try again.")
        if len(puter_word) > 6:
            print(f"So the FIRST TWO letters of the word are these: {puter_word[0:2]}")
            guessing2 = input("Enter your guess: ")
            print(guessing2)
            if guessing2 == puter_word: 
                human += 1.5
                print("Man. I guess you got it.")
            else: 
                print(f"The word also contains this letter: {puter_word[3]}")
                guessing4 = input("Enter your guess: ")
                print(guessing4)
                if guessing4 == puter_word: 
                    print("Drat! How could you beat me!?")
                    human += 1
                elif query == "y":
                    print(f"The word also contains this letter: {puter_word[5]}")
                    guessing6 = input("Enter your guess: ")
                    if guessing6 == puter_word:
                        print("You got me beat...")
                        time.sleep(2)
                        print("BUT THAT WON'T HAPPEN AGAIN!")
                        human += 1 
                    else:
                        print(f"The round for this game is over. The word was '{puter_word}'.")
                        time.sleep(1)
                        print("It's men versus machines, baby! And I WON!")
                        machine += 1 
                else: 
                    print(f"This round of the game is over. The word was '{puter_word}'.")
                    time.sleep(1)
                    print("I win, you lose. Loser.")
                    machine += 1 
        elif len(puter_word) <= 6: 
            print(f"The word also contains this letter: {puter_word[2]}")
            guessing3 = input("Enter your guess: ")
            print(guessing3)
            if guessing3 == puter_word: 
                print("You win this round...")
                time.sleep(2)
                print("BUT I'LL GET YOU NEXT TIME!")
                human += 1.5
            else:
                print(f"The word also contains this letter: {puter_word[3]}")
                guessing5 = input("Enter your guess: ")
                print(guessing5)
                if guessing5 == puter_word:
                    print("You got me beat...")
                    time.sleep(2)
                    print("BUT THAT WON'T HAPPEN AGAIN!")
                    human += 1 
                else:
                    print(f"The round for this game is over. The word was '{puter_word}'.")
                    time.sleep(1)
                    print("It's men versus machines, baby! And I WON!")
                    machine += 1 
    round_count += 1
else: 
    print("TOTAL SCORE:")
    time.sleep(1)
    print(f"computer: {machine}")
    print(f"player: {human}")
    if machine > human:
        print("HAHAHAHAHAHAHAHAHAHAHAHAHAH I WIN!!!!!!! YOU SUCK!!!!!! GAME OVERRRRRR!!")
    elif human > machine: 
        print("Ugh...you win. Darn...Never realised it would come to this...")
    elif human == machine:
        print("Tie?!?! But I was this close! THIS close!")
# note to self: it's not fair yet, but it's cooking. 
# might add easter eggs, like i want it to be offended if you can push its buttons 
# in particular ways. 
# another note to self: maybe make the third hint random. 

# another hint to self: i want the player to be able to choose different game modes, 
# and to display this on a website (with html)

# considering maybe an easy mode, normal mode, and hard mode. 
# also considering a timed mode. 
# and maybe a mode where the goal is merely to reach a certain amounts of points. hmm...

# maybe implement switch statements for readability 