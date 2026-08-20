# array, lambda, function, module, package

'Modules'
PI = 3.14159

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    return a / b


def floor_divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    return a // b


def modulus(a, b):
    if b == 0:
        print("Cannot modulo by zero.")
    return a % b


def power(base, exp):
    return base**exp


def negate(a):
    return -a


def absolute(a):
    return abs(a)

