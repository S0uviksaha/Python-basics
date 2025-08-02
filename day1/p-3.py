# type conversion

oldAge = input("Enter your age: ")
# input() returns a string, so we need to convert it to an integer (type conversion)
newAge = int(oldAge) + 1
print("Your age next year will be:", newAge)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2  # This will concatenate the strings
print("Sum of the two numbers is:", sum)

print("Sum of the two numbers is:", int(num1) + int(num2))  # Correct way to sum integers   

# print("Sum of the two numbers is:" + int(num1) + int(num2))  # This will concatenate the strings, not sum them, error will occur