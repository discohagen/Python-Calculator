from helpers import getLastCharacter


def calculator(exp: str) -> str:
    if exp == "":
        return ""

    lastCharacter = getLastCharacter(exp)
    match lastCharacter:
        case "x" | "÷" | "+" | "-" | ",":
            exp = exp[:-1]

    exp = exp.replace(",", ".")

    indexExp = 0
    while indexExp < len(exp):
        if exp[indexExp] == "x" or exp[indexExp] == "÷":

            innerIndex = indexExp - 1
            while innerIndex >= 0 and (exp[innerIndex].isdigit() or exp[innerIndex] == "."):
                innerIndex -= 1
            leftOperand = exp[innerIndex+1 : indexExp]

            innerIndex = indexExp + 1
            while innerIndex < len(exp) and (exp[innerIndex].isdigit() or exp[innerIndex] == "."):
                innerIndex += 1
            rightOperand = exp[indexExp+1 : innerIndex]

            if exp[indexExp] == "x":
                result = float(leftOperand) * float(rightOperand)
            elif exp[indexExp] == "÷":
                try:
                    result = float(leftOperand) / float(rightOperand)
                except:
                    print("somebody wanted to divide by 0")
                    return

            exp = exp.replace(leftOperand + exp[indexExp] + rightOperand, str(result), 1)

            indexExp = innerIndex - len(str(rightOperand)) - 1

        indexExp += 1

    indexExp = 0
    while indexExp < len(exp):
        if exp[indexExp] == "+" or exp[indexExp] == "-":

            innerIndex = indexExp - 1
            while innerIndex >= 0 and (exp[innerIndex].isdigit() or exp[innerIndex] == "."):
                innerIndex -= 1
            leftOperand = exp[innerIndex+1 : indexExp]

            innerIndex = indexExp - 1
            while innerIndex < len(exp) and (exp[innerIndex].isdigit() or exp[innerIndex] == "."):
                innerIndex += 1
            rightOperand = exp[indexExp+1 : innerIndex]

            if exp[indexExp] == "+":
                result = float(leftOperand) + float(rightOperand)
            elif exp[indexExp] == "-":
                result = float(leftOperand) - float(rightOperand)

            exp = exp.replace(leftOperand + exp[indexExp] + rightOperand, str(result), 1)

            indexExp = innerIndex - len(str(rightOperand)) - 1

        indexExp += 1

    exp = exp.replace(".", ",")
    
    return exp