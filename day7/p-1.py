# Functions

# 1. User defined function
# 2. Built-in function
# 3. Module function


# Built-in function
input_value = input("Enter a value: ")  # Built-in function to take user input
print("You entered:", input_value)
print(int(input_value)) # Convert input to integer using built-in function


# Module function
import math  # Importing the math module
print(dir(math))  # Display all functions in the math module
print(math.sqrt(16))
print(math.pi)

from math import sqrt
print(sqrt(16))

from math import *
print(sqrt(16))
print(factorial(5)) 


# User defined function

def print_Sum(a, b):
    print("Sum is:", a + b)

print_Sum(10, 20)  # Calling the user-defined function with arguments