from flask import Flask
from flask import render_template

def calculator():
    return

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "calculator.html",

    )