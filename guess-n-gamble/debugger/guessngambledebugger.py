#!/usr/bin/env python3 

# importing necessary packages
from flask import Flask, render_template, request

# flask gobbledygook
app = Flask(__name__)
app.secret_key = "2ykrj6ujukgwe8kvbvxssmffxty9j9"
app.run(host='0.0.0.0', debug=True)

@app.route("/", methods=["GET","POST"])
def index():
    instruction_answer = request.form.get("instruction_answer", "")
    if request.method=="POST": # this line is added. will have to add everywhere probably. 
        while instruction_answer not in ["y", "n"]:
            instruction_message = "Please enter y or n, lowercase with no spaces or punctuation:\n"
            # removed the variable instruction_answer defined here. (chatgpt suggestion)
            return render_template("silly.html", 
            message=instruction_message)  
        if instruction_answer == "y":
            return render_template("silly.html")
        elif instruction_answer == "n":
            return render_template("index.html", message="Okay. Good luck!")
        
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/silly", methods="GET")
def game_round():
    return render_template("silly.html")
