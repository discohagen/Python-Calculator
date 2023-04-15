from flask import Flask, render_template, request

calculationInput = "test"

calculationOutput = "0"

def calculator(input):
    return

app = Flask(__name__)

@app.route("/")
def home():
    context = {"input": calculationInput, "output": calculationOutput}

    return render_template(
        "calculator.html",
        **context
    )