num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter opertion (+, -, *, /):")

if operation == "+":
    result = num1 + num2
elif operation ==  "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invaild operation"

print("Result:", result)
