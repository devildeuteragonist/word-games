#!/usr/bin/env python3


### NEEDS SIGNIFICANT WORK ###
### NEEDS SIGNIFICANT WORK ###
### NEEDS SIGNIFICANT WORK ###

# IM APPARENTLY USING MY GITHUB CODESPACES LIMIT REALLY REALLY QUICKLY SO I'M JUST GONNA HAVE TO MODIFY THIS LOCALLY NOW. 

# importing necessary packages
from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request
import time
import random

# flask gobbledygook
app = Flask(__name__)
app.secret_key = "funfunfun"

@app.route("/")
def index():
    instruction_answer = request.form["instruction_answer"]
    while instruction not in ["y", "n"]:
        instruction = input("Please enter y or n, lowercase with no spaces or punctuation: ")
    if instruction_answer == "y":
        return render_template("instructions.html")
    elif instruction_answer == "n":
        return render_template("index.html", message="Okay. Good luck!") # this is WRONG 
# instructions yes or no, error handling not done well up here. ^ 

if __name__ == "__main__":
    app.run(debug=True)

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

@app.route("/instructions")
# this needs work. and buttons. 

@app.route("/start", methods=["POST"])
def start_game():
# setting the starting number of points for both human and machine
    session["machine"] = 0 
    session ["human"] = 0          
# setting quantities for number of rounds and hints
    session["round_count"] = 1      
    session["total_rounds"] = 20
    session["hint_use_counter"] = 0
# redirect code to actual game  
    return redirect(url_for('game_round'))


# creating function to define hints (jazakhallah khair chatgpt)
def generate_hints(chosen_word):
    return [
        f"The second letter of the word is this: {chosen_word[1]}", 
        f"The third letter of the word is this: {chosen_word[2]}", 
        f"The fourth letter of the word is this: {chosen_word[3]}"
    ]

# game
@app.route('/game_round', methods=['GET', 'POST'])
def game_round():
    if session["round_count"] > session["total_rounds"]:
        return redirect(url_for("end_game"))  
    
    # computer chooses a word  
    session["puter_word"] = random.choice(words)
    # defining our hints 
    hints = generate_hints(session["puter_word"])
    # defining possible amounts of points to wager 
    if len(session["puter_word"]) < 9:
        points_to_wager = 1 # ah dang it!
        points_to_earn = 3 # i can't stop winning!
    elif len(session["puter_word"]) >= 9:
        points_to_wager = 2 # ah dang it! 
        points_to_earn = 5 # i can't stop winning! 

    '''
    ALL OF THIS BELOW WILL ACTUALLY BE ON OUR HTML DOCUMENT. 
    # round/point counter for the reference of the player
    time.sleep(2)
    print(f"ROUND {session["round_count"]} OF 20 STARTS")
    time.sleep(0.5)
    print(f"player {session["human"]} points, computer {session["machine"]} points")  
    '''    

    # below is the initial hint (the start and end letters of the word and its length)
    # it is to be printed before the player makes their first guess. 
    '''
    # computer prompts YOU to guess what it's saying. in the final code, none of these will be printed.  
    print(random.choice(robot_rizz))
    time.sleep(1)
    print("...")
    time.sleep(0.5)
    print(f"I'm thinking of a word that is {len(session["puter_word"])} letters long...") 
    print(f"...that starts with {session["puter_word"][0]} and ends with {session["puter_word"][-1]}.")
    time.sleep(0.5)
    '''
    
    # asking if the player if they want to G A M B L E. in the final code, none of these will be printed. 
    if len(session["puter_word"]) > 6: 
        wager_message_1 = f"Want an extra hint this round for {points_to_wager}?\nIf you're successful, you gain {points_to_earn} points back. y/n:"
        wager_answer = request.form["wager_answer"]
        while wager_answer not in ["y", "n"]:
            wager_message_2 = "Please enter y or n, lowercase with no spaces or punctuation: "
            wager_answer = request.form["wager_answer"]
            return render_template("game_round.html", 
            message=wager_message_2, 
            round=session["round_count"], 
            human=session["human"], 
            machine=session["machine"]
            )  
        if wager_answer == "y":
            session["human"] -= points_to_wager
        elif wager_answer == "n": 
            session["human"] += 0
    else:
        wager_message_2 = "No hints are available to gamble for words six letters long or less."
        session["human"] += 0
        return render_template("game_round.html", 
        message=wager_message_2, 
        round=session["round_count"], 
        human=session["human"], 
        machine=session["machine"]
        )  

    # we'd need to clear the page and then load new stuff happening on the page maybe. 

    # initial guess 
    if request.method == 'POST':
        user_guess = request.form["user_guess"]

    # handling subsequent guesses 
    if user_guess == session["puter_word"]: 
        session["human"] += 2
        return render_template("game_round.html", message="Ugh. Can't believe you managed to get me this early...") 
    else: 
        # the actual subsequent-guesses-and-hint process
        if wager_answer == "y":
            while hint_use_counter < 5:
                # thank you chatgpt for showing me how to do the render_template thing not seven million times
                hint_message = f"Hint {hint_use_counter + 1} out of 4: {random.choice(hints)}\n Enter your guess:" if hint_use_counter < 4 else "No more hints available."
                user_guess_2 = request.form["user_guess_2"]
                hint_use_counter += 1
                if user_guess_2 == session["puter_word"]:
                    session["human"] += points_to_earn 
                    return render_template("game_round.html", message=random.choice(human_success))  
                elif hint_use_counter == 5:
                    session["machine"] += 1 
                    return render_template("game_round.html", message=f"The word was {session["puter_word"]}.\n{random.choice(computer_taunts)}")
        elif wager_answer == "n":
            while hint_use_counter < 4:
                hint_message = f"Hint {hint_use_counter + 1} out of 3: {random.choice(hints)}\n Enter your guess:" if hint_use_counter < 3 else "No more hints available."
                user_guess_2 = request.form["user_guess_2"]
                hint_use_counter += 1
                if user_guess_2 == session["puter_word"]:
                    session["human"] += 2-(hint_use_counter*0.25)
                    return render_template("game_round.html", message=random.choice(human_success), word=session["puter_word"], round=session["round_count"], human=session["human"], machine=session["machine"])
                elif hint_use_counter == 4:
                    session["machine"] += 1 
                    return render_template("game_round.html", message=f"The word was {session["puter_word"]}.\n{random.choice(computer_taunts)}")
    hint_use_counter = 1
    session["round_count"] += 1
    return render_template("game_round.html", 
    message=hint_message, 
    round=session["round_count"], 
    hint_use_counter=hint_use_counter, 
    human=session["human"], 
    machine=session["machine"]
    )


# game ending 
@app.route('/end_game')
def end_game():
    scores = f"computer: {session["machine"]}\nplayer: {session["human"]}"
    if session["machine"] > session["human"]:
        end_message = "HAHAHAHAHAHAHAHAHAHAHAHAHAH I WIN!!!!!!! YOU SUCK!!!!!! GAME OVERRRRRR!!"
    elif session["human"] > session["machine"]: 
        end_message = "Ugh...you win. Darn...Never realised it would come to this..."
    elif session["human"] == session["machine"]:
        end_message = "Tie?!?! But I was this close! THIS close!"
    return render_template("end_game.html", message=(scores + end_message))
