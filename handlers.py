def handleInput(state: str, input : str) -> str:

    match input:
        case unused if input.isnumeric():
            return state + input
        
        case "C":
            return ""

        case "+/-":
            return handleChangeSign(state)
        
        case "%":
            return handlePercentage(state)
        
        case "x" | "÷" | "+" | "-":
            return handleOperator(state, input)
        
        case ",":
            return handleComma(state)
        
        case "=":
            return calculator(state)

        case _ :
            print("something went wrong")
            return

def handleChangeSign(exp) -> str:
    lastCharacter = getLastCharacter(exp)
    
    match lastCharacter:
        case "":
            return "-"
        
        case "+":
            return exp[:-1] + "-"
        
        case "-":
            if len(exp) == 1:
                return ""
            else:
                return exp[:-1] + "+"
            
        case "÷" | "x" | ",":
            return exp
        
        case unused if lastCharacter.isnumeric():
            return exp + "-"
        
        case _:
            print("something went wrong")
            return

def handlePercentage(exp) -> str:
    lastCharacter = getLastCharacter(exp)

    match lastCharacter:
        case "":
            return ""
        
        case "+" | "-" | "÷" | "x" | ",":
            return exp

        case unused if lastCharacter.isnumeric():
            lastNumber = getLastNumber(exp)
            lastNumber = lastNumber.replace(",", ".")

            lastNumberPercentage = (str(float(lastNumber) / 100)).replace(".", ",")
            if lastNumberPercentage[-1] == "0":
                lastNumberPercentage = lastNumberPercentage[:-2]

            return exp[:-len(lastNumber)] + lastNumberPercentage

        case _:
            print("something went wrong")
            return

def handleOperator(exp, input):
    lastCharacter = getLastCharacter(exp)

    match lastCharacter:
        case "":
            if input == "-":
                return "-"
            return ""

        case "+" | "-" | "÷" | "x" | ",":
            return input
        
        case unused if lastCharacter.isnumeric():
            return exp + input

        case _:
            print("something went wrong")
            return

def handleComma(exp) -> str:
    return

def calculator(exp: str) -> str:
    return

def getLastCharacter(exp) -> str:
    if exp == "":
        lastCharacter = exp
    else : 
        lastCharacter = exp[-1]

    return lastCharacter

def getLastNumber(exp) -> str:
    reverse = exp[::-1]
    lastNumber = ""

    for char in reverse:
        if char.isnumeric() or char == ",":
            lastNumber += char
        else:
            break

    return lastNumber[::-1]