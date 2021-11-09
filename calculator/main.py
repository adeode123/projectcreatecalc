""" Calculator """
class Calculator:

    def __init__(self,first_num,second_num):
        self.first_num = first_num
        self.second_num = second_num
        self.history = []

    def get_history(self):
        return self.history

    def get_last_calculation(self):
        return self.history[-1]

    def get_first_calculation(self):
        return self.history[0]

    def add_calculation_to_history(self, record):
        self.history.append(record)

    def get_last_calculation_result(self):
        return None

    def last_calculation_object(self):
        return None

    def clear_history(self):
        self.history = []

    def count_history(self):
        return len(self.history)


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
