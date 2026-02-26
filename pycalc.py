
def calcul(number1,signe,number2):
    if signe == "+":
        return number1 + number2
    elif signe == "-":
        return number2 - number1
    elif signe == "/":
        return number1 / number2
    elif signe == "*":
        return number1 * number2 
    else:
        print("nah")
a = calcul(420, "+", 67)

print(a)
