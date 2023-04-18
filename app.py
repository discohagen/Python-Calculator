from flask import Flask, render_template, request

from handlers import handleInput 

"""
def handleInput(state : str, newStateToGetChecked : str) -> str:

    newCharacter = newStateToGetChecked[-1]

    if state == "":
        lastCharacter = state
    else : 
        lastCharacter = state[-1]

    match newCharacter:
        case unused if newCharacter.isnumeric():
            return newStateToGetChecked
        
        case "C":
            return ""
        
        case "+/-":
            if state == "-":
                return ""
                        
            match lastCharacter:
                case "":
                    return "-"
                case "+":
                    return state[0, len(state) - 1] + "-" 
                case "÷" | "x":
                    return state
                case "-":
                    return state[0, len(state) - 1] + "+"
                case _: #equal to lastCharacter being numeric
                    return #WIP: change sign of the last numeric expression
                
        case "%":
            match lastCharacter:
                case "":
                    return ""
                case "÷" | "x" | "+" | "-":
                    return state
                case _:
                    lastNumber = getLastNumber(state)
                    return (
                        state[0, len(state) - len(lastNumber)] 
                        +  str(int(lastNumber) / 100)
                    )
        
        case "÷" | "x" | "+" | "-":
            match lastCharacter:
                case "":
                    return ""
                case unused if lastCharacter.isnumeric():
                    return newStateToGetChecked
                case _:
                    return state[0, len(state) - 1] + lastCharacter
        
        case ",":
            match lastCharacter:
                case "":
                    return "0,"
                case unused if lastCharacter.isnumeric():
                    return newStateToGetChecked
                case _:
                    return state + "0,"

        case "=":
            return calculator(state)

        case _:
            return state
"""

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