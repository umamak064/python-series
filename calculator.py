#Simple Calculator
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))

operation= input("Choose Operation to perform: ")

if operation == "+":
    sum = num1+ num2
    print(sum)
elif  operation == "-":
    sub = num1 - num2
    print(sub)   
elif  operation == "*":
    multiply = num1 * num2
    print(multiply) 
elif  operation == "/":
    if num2 != 0:
        divide = num1 / num2
        print(divide) 
    else:
        print("Division by zero is not allowed")
else:
    print("invalid")


