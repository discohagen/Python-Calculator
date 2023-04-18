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
            lastNumber, isDecimal = getLastNumberAndType(exp)


            if isDecimal:
                return #WIP
            else: 
                lastNumberPercentage = (str(int(lastNumber) / 100)).replace(".", ",")
                if lastNumberPercentage[-1] == "0":
                    lastNumberPercentage = lastNumberPercentage[:-2]

                return exp[:-len(lastNumber)] + lastNumberPercentage

        case _:
            print("something went wrong")
            return

def handleOperator(exp, input):
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

def getLastNumberAndType(exp) -> tuple:
    reverse = exp[::-1]
    lastNumber = ""
    isDecimal = False

    for char in reverse:
        if char.isnumeric():
            lastNumber += char
        elif char == ",":
            lastNumber += char
            isDecimal = True
        else:
            break

    return lastNumber[::-1], isDecimal