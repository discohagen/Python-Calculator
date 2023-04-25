from flask import Flask, render_template, request

from handlers import handleInput 

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

    newState = handleInput(state, request.form.get("input"))

    context = {"input": newState, "output": 0}

    return render_template(
        "calculator.html",
        **context
    )