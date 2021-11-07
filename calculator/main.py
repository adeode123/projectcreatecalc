# Calculator
# Test for addition
def add(first_num, second_num):
    return first_num + second_num


# Test for subtraction
def subtract(first_num, second_num):
    return first_num - second_num


# Test for multiplication
def multiply(first_num, second_num):
    return first_num * second_num


# Test for division
def divide(first_num, second_num):
    try:
        return first_num/second_num
    except ZeroDivisionError:
        print("division by zero is not allowed")
