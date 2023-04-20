from handlers import getLastCharacter


def calculator(exp: str) -> str:
    if exp == "":
        return ""

    lastCharacter = getLastCharacter(exp)
    match lastCharacter:
        case "x" | "÷" | "+" | "-" | ",":
            exp = exp[:-1]

    exp = exp.replace(",", ".")

    numbers = exp
    for char in ["x", "÷", "+", "-"]:
        numbers = numbers.replace(char, " ")

    numbersList = numbers.split()

    