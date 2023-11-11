# calculator_operations.py

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base):
    return math.log(x, base)

def factorial(x):
    return math.factorial(x)

def absolute_value(x):
    return abs(x)

def gcd(x, y):
    return math.gcd(int(x), int(y))

def lcm(x, y):
    return abs(x * y) // math.gcd(int(x), int(y))

def round_number(x, decimal_places=0):
    return round(x, decimal_places)

def permutations(n, r):
    return math.perm(n, r)

def combinations(n, r):
    return math.comb(n, r)


# main_calculator.py
from calculator_operations import *

def calculator():
    print("Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")
    print("12. Absolute Value")
    print("13. Greatest Common Divisor (GCD)")
    print("14. Least Common Multiple (LCM)")
    print("15. Round Number")
    print("16. Permutations")
    print("17. Combinations")

    choice = input("Enter choice (1-17): ")

    if choice not in map(str, range(1, 18)):
        print("Invalid Input")
        return

    if choice in map(str, range(1, 14)):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    elif choice in map(str, range(14, 18)):
        num1 = float(input("Enter the number: "))
        num2 = None

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "^", num2, "=", power(num1, num2))
    elif choice == '6':
        print("Square root of", num1, "=", sqrt(num1))
    elif choice == '7':
        print("Sine of", num1, "degrees =", sin(num1))
    elif choice == '8':
        print("Cosine of", num1, "degrees =", cos(num1))
    elif choice == '9':
        print("Tangent of", num1, "degrees =", tan(num1))
    elif choice == '10':
        base = float(input("Enter the base: "))
        print("Logarithm of", num1, "with base", base, "=", log(num1, base))
    elif choice == '11':
        print("Factorial of", num1, "=", factorial(num1))
    elif choice == '12':
        print("Absolute value of", num1, "=", absolute_value(num1))
    elif choice == '13':
        print("GCD of", num1, "and", num2, "=", gcd(num1, num2))
    elif choice == '14':
        print("LCM of", num1, "and", num2, "=", lcm(num1, num2))
    elif choice == '15':
        decimal_places = int(input("Enter the number of decimal places: "))
        print("Rounded value of", num1, "is", round_number(num1, decimal_places))
    elif choice == '16':
        r = int(input("Enter the number of permutations (r): "))
        print("Permutations of", num1, "with", r, "elements is", permutations(num1, r))
    elif choice == '17':
        r = int(input("Enter the number of combinations (r): "))
        print("Combinations of", num1, "with", r, "elements is", combinations(num1, r))

    # more cases will be add soon...

calculator()
