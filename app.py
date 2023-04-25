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

# Find all addition and subtraction operations
    result = 0
    i = 0
    operator = "+"
    while i < len(exp):
        if exp[i] == "+" or exp[i] == "-":
            # Get the left operand
            j = i - 1
            while j >= 0 and (exp[j].isdigit() or exp[j] == "."):
                j -= 1
            leftOperand = float(exp[j+1:i])
            
            # Update the result based on the previous operator
            if operator == "+":
                result += leftOperand
            else:
                result -= leftOperand
                
            # Update the operator
            operator = exp[i]
            
        i += 1
    
    # Get the last operand and update the result
    j = len(exp) - 1
    while j >= 0 and (exp[j].isdigit() or exp[j] == "."):
        j -= 1
    lastOperand = float(exp[j+1:])
    if operator == "+":
        result += lastOperand
    else:
        result -= lastOperand
        
    return str(result).replace(".", ",")