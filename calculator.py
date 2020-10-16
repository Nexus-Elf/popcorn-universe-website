number1  = float(input("Please enter your first number:"))
Operator = input("Please enter your Mathematical Operator:")
number2 = float(input("Please enter your second number:"))

if Operator == "+":
        print(number1 + number2)
    elif Operator == "-":
        print(number1 - number2)
    elif Operator == "*":
        print(number1 * number2)
    elif Operator == "/":
        print(number1 / number2)
else:
    print("Please Enter a valid Mathematical Operator: (e.g +, -, *, /)")


        
