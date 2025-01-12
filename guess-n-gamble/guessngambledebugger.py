# importing necessary packages
from flask import Flask, render_template, request, session, redirect, url_for

# flask gobbledygook
app = Flask(__main__)
app.secret_key = "2ykrj6ujukgwe8kvbvxssmffxty9j9"
app.run(host='0.0.0.0', debug=True)

@app.route("/", methods=["GET","POST"])
def index():
    instruction_answer = request.form.get("instruction_answer", "")
    while instruction_answer not in ["y", "n"]:
        instruction_message = "Please enter y or n, lowercase with no spaces or punctuation:\n"
        instruction_answer = request.form["instruction_answer"]
        return render_template("game_round.html", 
        message=instruction_message)  
    if instruction_answer == "y":
        return render_template("instructions.html")
    elif instruction_answer == "n":
        return render_template("index.html", message="Okay. Good luck!")
        
if __name__ == "__main__":
    app.run(debug=True)
