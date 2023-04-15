from flask import Flask, render_template, request

def checkState(state):
    return

def calculator(input):
    return

app = Flask(__name__)

@app.get("/")
def home_get():
    context = {"input": "", "output": 0}

    return render_template(
        "calculator.html",
        **context
    )

@app.post("/")
def home_post():
    state = request.form.get("state", default="")

    state = state + request.form.get("input")

    context = {"input": state, "output": 0}

    return render_template(
        "calculator.html",
        **context
    )