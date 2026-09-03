num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operation = input("Choose operation(+, -, *, /): ")
if operation == "+":
    print("Result =", num1 + num2)
elif operation == "-":
    print("Result =", num1 - num2) 
elif operation == "*":
    print("Result =", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Not divisible by 0 ")
else:
    print("Wrong operation ")