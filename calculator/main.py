# Calculator
# Test for addition
def add(a, b):
    return a + b


# Test for subtraction
def subtract(a, b):
    return a - b


# Test for multiplication
def multiply(a, b):
    return a * b


# Test for division
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("division by zero is not allowed")
