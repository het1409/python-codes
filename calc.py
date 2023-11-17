n1 = float(input("Enter number: "))
n2 = float(input("Enter number: "))

operation = input("Type +, -, /, *: ")

if operation == "+":
    result = n1 + n2
    print(result)
elif operation == "-":
    result = n1 - n2
    print(result)
elif operation == "/":
    result = n1 / n2
    print(result)
else:
    result = n1 * n2
    print(result)