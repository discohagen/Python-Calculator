from helpers import getLastCharacter


def calculator(exp: str) -> str:
    if exp == "":
        return ""

    lastCharacter = getLastCharacter(exp)
    match lastCharacter:
        case "x" | "÷" | "+" | "-" | ",":
            exp = exp[:-1]

    exp = exp.replace(",", ".")

    i = 0
    while i < len(exp):
        if exp[i] == "x" or exp[i] == "÷":

            j = i - 1
            while j >= 0 and (exp[j].isdigit() or exp[j] == "."):
                j -= 1
            leftOperand = (exp[j+1 : i])

            j = i + 1
            while j < len(exp) and (exp[j].isdigit() or exp[j] == "."):
                j += 1
            rightOperand = (exp[i+1 : j])

            if exp[i] == "x":
                result = float(leftOperand) * float(rightOperand)
            elif exp[i] == "÷":
                try:
                    result = float(leftOperand) / float(rightOperand)
                except:
                    print("somebody wanted to divide by 0")
                    return

            exp = exp.replace(leftOperand + exp[i] + rightOperand, str(result), 1)

            i = j - len(str(rightOperand)) - 1

        i += 1

    i = 0
    while i < len(exp):
        if exp[i] == "+" or exp[i] == "-":

            j = i - 1
            while j >= 0 and (exp[j].isdigit() or exp[j] == "."):
                j -= 1
            leftOperand = exp[j+1 : i]

            j = i - 1
            while j < len(exp) and (exp[j].isdigit() or exp[j] == "."):
                j += 1
            rightOperand = exp[j+1 : i]

            if exp[i] == "+":
                result = float(leftOperand) + float(rightOperand)
            elif exp[i] == "-":
                result = float(leftOperand) - float(rightOperand)

            exp = exp.replace(leftOperand + exp[i] + rightOperand, str(result), 1)

            i = j - len(str(rightOperand)) - 1

        i += 1

    exp = exp.replace(".", ",")
    
    return exp