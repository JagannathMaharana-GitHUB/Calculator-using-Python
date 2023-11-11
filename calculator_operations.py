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

