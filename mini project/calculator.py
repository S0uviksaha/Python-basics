# Calculator Application

input("Welcome to the Calculator App! Press Enter to start...")
num1 = input("Enter the first number: ")
opertor = input("Enter an operator (+, -, *, /): ")
num2 = input("Enter the second number: ")

if opertor == "+":
    result = float(num1) + float(num2)
elif opertor == "-":
    result = float(num1) - float(num2)  
elif opertor == "*":
    result = float(num1) * float(num2)
elif opertor == "/":
    if float(num2) != 0:
        result = float(num1) / float(num2)
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."

print("The result is:", result)
input("Press Enter to exit the Calculator App.")
