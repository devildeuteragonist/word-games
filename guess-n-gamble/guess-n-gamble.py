#!/usr/bin/env python3

# importing necessary packages
from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request
import time
import random

# flask gobbledygook
app = Flask(__name__)
app.secret_key = "funfunfun"

@app.route('/')
def index():
    return render_template("guessngamble.html")

if __name__ == "__main__":
    app.run(debug=True)

# all my code needs far more work bearing in mind i want to display it now. 
#### I HOPE TO CLEAN THIS ALL UP ####

# importing those 5000 most common words
url = "https://raw.githubusercontent.com/devildeuteragonist/word-games/refs/heads/main/guess-n-gamble/5000-common-words.txt"
with urllib.request.urlopen(url) as f: 
    words = f.read().decode("utf-8").splitlines() 

# cleaning the file of words three letters or shorter 
our_words = [word for word in words if len(word) > 4 and len(word) < 12]
    # there are brackets here so python knows we are dealing with 
    # a list. this is so we don't have to use a for loop because 
    # we are cute and smart like that. 
 
# let's give our computer some...personality.
# starting message for a round 
robot_rizz = ["Ya think you can play against me?", "My riddles will twist your squishy flesh-brain into a pretzel!",
    "You've decided to be my opponent? How daring.", "You're naive enough to think you can beat me. It sure shows, kid.",
    "Kahahaha! Beating you will be fun."]
# responses if success or loss  
computer_taunts = ["It's men versus machines, baby!\nAnd I WON!", "I win, you lose. Loser."]
human_success = ["Man. I guess you got it.", "Ugh! You got me!", 
                 "Drat! How could you beat me!?", "You got me beat...\nBUT THAT WON'T HAPPEN AGAIN!"]


@app.route("/start", methods=["POST"])
def start_game():
# setting the starting number of points for both human and machine
    session["machine"] = 0 
    session ["human"] = 0          
# setting quantities for number of rounds and hints
    session["round_count"] = 1      
    session["total_rounds"] = 20
    session["hint_use_counter"] = 1

# instructions yes or no
instruction = input("(This is the programmer speaking.\nDo you need instructions for The Guessing Game?) y/n: ")
while instruction not in ["y", "n"]:
    instruction = input("Please enter y or n, lowercase with no spaces or punctuation: ")
if instruction == "y":
    print("(You are given 15 seconds to read the following instructions\nbefore the game starts:)")
    time.sleep(1)
    print("===================================================================================")
    print("(This game is best played with a pencil and paper in hand.\nPlease do not look up any words. That is cheating!)")
    print("(Input is case-sensitive, and sensitive to SPACES and OTHER CHARACTERS!\nThe computer is also extremely obnoxious and I hate him.)")
    print("Sometimes, you are given the chance to gamble some points for an extra hint.")
    print("As you use more hints in a round, the points you earn back are reduced if you succeed.\nPoints earned back from wagering are protected from this.")
    print("===================================================================================")
    time.sleep(15)
elif instruction == "n": 
    print("(Okay. Good luck!)")

# game
@app.route('/game_round', methods=['GET', 'POST'])
def game_round():
    while session["round_count"] <= session["total_rounds"]:
        # computer chooses a word  
        session["puter_word"] = random.choice(words)

        # defining our hints 
        hints = [f"The second letter of the word is this: {session["puter_word"][1]}", 
            f"The fourth letter of the word is this: {session["puter_word"][3]}",
            f"The third letter of the word is this: {session["puter_word"][2]}"]
        if request.method == 'POST':
            user_guess = request.form['guess']

            # defining possible amounts of points to wager
            # LET'S GO GAMBLING! AH DANG IT! AH DANG IT! AH DANG IT!
            if len(session["puter_word"]) < 9:
                points_to_wager = 1 # ah dang it!
                points_to_earn = 3 # i can't stop winning!
            elif len(session["puter_word"]) >= 9:
                points_to_wager = 2 # ah dang it! 
                points_to_earn = 5 # i can't stop winning! 

            # round/point counter for the reference of the player
            time.sleep(2)
            print(f"ROUND {session["round_count"]} OF 20 STARTS")
            time.sleep(0.5)
            print(f"player {session["human"]} points, computer {session["machine"]} points")      
            
            # computer prompts YOU to guess what it's saying 
            print(random.choice(robot_rizz))
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            print(f"I'm thinking of a word that is {len(session["puter_word"])} letters long...")
            print(f"...that starts with {session["puter_word"][0]} and ends with {session["puter_word"][-1]}.")
            time.sleep(0.5)
            
            # asking if the player if they want to G A M B L E 
            if len(session["puter_word"]) > 6: 
                print(f"Want an extra hint this round for {points_to_wager}?") 
                query = input(f"If you're successful, you gain {points_to_earn} points back. y/n: ")
                while query not in ["y", "n"]:
                    query = input("Please enter y or n, lowercase with no spaces or punctuation: ")
                if query == "y":
                    session["human"] -= points_to_wager
                elif query == "n": 
                    session["human"] += 0
                    time.sleep(0.25)
                    print("...")
                    time.sleep(0.5)
            else:
                print("No hints are available to gamble for words six letters long or less.")
                query = "n"
            guessing = input("Enter your guess: ")


            # handling subsequent guesses 
            if guessing == session["puter_word"]: 
                print("Ugh. Can't believe you managed to get me this early...")
                session["human"] += 2 
            else: 
                print("Ha! Try again.")
                # the actual subsequent-guesses-and-hint process
                if query == "y":
                    while hint_use_counter < 5:
                        print(f"hint {hint_use_counter} out of 4")
                        guessing2 = input(f"Here's a hint. {random.choice(hints)}\n Enter your guess:")
                        hint_use_counter += 1
                        if guessing2 == session["puter_word"]:
                            print(random.choice(human_success))
                            session["human"] += points_to_earn  
                            break
                        elif hint_use_counter == 5:
                            print(f"The word was {session["puter_word"]}.")
                            time.sleep(0.25)
                            print(random.choice(computer_taunts))
                            session["machine"] += 1 
                            break
                elif query == "n":
                    while hint_use_counter < 4:
                        print(f"hint {hint_use_counter} out of 3")
                        guessing2 = input(f"Here's a hint. {random.choice(hints)}\n Enter your guess:")
                        hint_use_counter += 1
                        if guessing2 == session["puter_word"]:
                            print(random.choice(human_success))
                            session["human"] += 2-(hint_use_counter*0.25)
                            break
                        elif hint_use_counter == 4:
                            print(f"The word was {session["puter_word"]}.")
                            time.sleep(0.25)
                            print(random.choice(computer_taunts))
                            session["machine"] += 1 
                            break
            hint_use_counter = 1
            session["round_count"] += 1


    # game ending 
    else: 
        @app.route('/end_game')
        def end_game():
            print("TOTAL SCORE:")
            time.sleep(1)
            print(f"computer: {session["machine"]}")
            print(f"player: {session["human"]}")
            if session["machine"] > session["human"]:
                print("HAHAHAHAHAHAHAHAHAHAHAHAHAH I WIN!!!!!!! YOU SUCK!!!!!! GAME OVERRRRRR!!")
            elif session["human"] > session["machine"]: 
                print("Ugh...you win. Darn...Never realised it would come to this...")
            elif session["human"] == session["machine"]:
                print("Tie?!?! But I was this close! THIS close!")
    # note to self: it's not fair yet, but it's cooking. 
    # might add easter eggs, like i want it to be offended if you can push its buttons 
    # in particular ways. 

    # another hint to self: i want the player to be able to choose different game modes, 
    # and to display this on a website (with html)

    # considering maybe an easy mode, normal mode, and hard mode. 
    # also considering a timed mode. 
    # and maybe a mode where the goal is merely to reach a certain amounts of points. hmm...