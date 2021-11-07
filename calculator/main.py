""" Calculator """

def add(first_num, second_num):
    """ Test for addition """
    return first_num + second_num


def subtract(first_num, second_num):
    """ Test for subtraction """
    return first_num - second_num


def multiply(first_num, second_num):
    """ Test for multiplication"""
    return first_num * second_num


def divide(first_num, second_num):
    """Test for division"""
    try:
        return first_num/second_num
    except ZeroDivisionError:
        print("division by zero is not allowed")
        return None
