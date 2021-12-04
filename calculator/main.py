from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division
from calculator.calculations.history import History

""" Calculator """


class Calculator:
    """ Calculator class """
    calculator_history = []

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    @staticmethod
    def get_history():
        """ History of calculator operations"""
        return Calculator.calculator_history

    @staticmethod
    def get_last_calculation():
        """ Get last calculations"""
        return Calculator.calculator_history[-1]

    @staticmethod
    def get_first_calculation():
        """ Get first calculations"""
        return Calculator.calculator_history[0]

    @staticmethod
    def add_calculation_to_history(record):
        """ Add calculations to calculations history """
        Calculator.calculator_history.append(record)
        return Calculator.calculator_history

    @staticmethod
    def get_last_calculation_result():
        """ Get last calculations result """
        return Calculator.calculator_history[-1].get("result", None)

    @staticmethod
    def get_last_calculation_object():
        """ Get last calculations object """
        return Calculator.calculator_history[-1].get("object", None)

    @staticmethod
    def clear_history():
        """ Clear history """
        Calculator.calculator_history = []
        return Calculator.calculator_history

    @staticmethod
    def count_history():
        """ Get count of history items """
        return len(Calculator.calculator_history)

    @staticmethod
    def addition(num_1, num_2):
        """ Add """
        return num_1 + num_2

    @staticmethod
    def add_numbers(numbers: tuple):
        calc = Addition(numbers)
        History.append_calculation(calc)
        return calc.get_result()

    @staticmethod
    def subtract_numbers(numbers: tuple):
        calc = Subtraction(numbers)
        History.append_calculation(calc)
        return calc.get_result()

    @staticmethod
    def multiply_numbers(numbers: tuple):
        calc = Multiplication(numbers)
        History.append_calculation(calc)
        return calc.get_result()

    @staticmethod
    def divide_numbers(numbers: tuple):
        calc = Division(numbers)
        History.append_calculation(calc)
        return calc.get_result()

    @staticmethod
    def subtraction(num_1, num_2):
        """ Subtract """
        return num_1 - num_2

    @staticmethod
    def multiplication(num_1, num_2):
        """ Multiplication """
        return num_1 * num_2

    @staticmethod
    def division(num_1, num_2):
        """ Division """
        try:
            return num_1 / num_2
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            return None

    def factory(self, operation):
        """ Factory helper method """
        if operation == 'add':
            add_object = Add(first_num=self.first_num, second_num=self.second_num)
            result = add_object.add()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": add_object
            })
            return result

        if operation == 'subtract':
            subtract_object = Subtract(first_num=self.first_num, second_num=self.second_num)
            result = subtract_object.subtract()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": subtract_object
            })
            return result

        if operation == 'multiply':
            multiply_object = Multiply(first_num=self.first_num, second_num=self.second_num)
            result = multiply_object.multiply()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": multiply_object
            })
            return result

        if operation == 'divide':
            divide_object = Divide(first_num=self.first_num, second_num=self.second_num)
            result = divide_object.divide()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": divide_object
            })
            return result

        return "Invalid Operation"


class Add(Calculator):
    """ Add inherited from Calculator"""

    def add(self):
        """ Add from child class"""
        return self.first_num + self.second_num


class Subtract(Calculator):
    """ Subtract inherited from Calculator """

    def subtract(self):
        """ Subtract from child class"""
        return self.first_num - self.second_num


class Multiply(Calculator):
    """ Multiply inherited from Calculator """

    def multiply(self):
        """ Multiply from child class """
        return self.first_num * self.second_num


class Divide(Calculator):
    """ Divide inherited from Calculator """

    def divide(self):
        """ Divide from child class """
        try:
            return self.first_num / self.second_num
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            return None

import pandas as pd

data = pd.read_csv("C:/Users/Abosede/PycharmProjects/calc_part2/tests/input_add.csv")
for index, row in data.iterrows():
    t = row
    size = len(t)
    operation = t.iloc[size - 1]
    if operation == 'add':
        result = Calculator.add_numbers(t)
        print(result)
    elif operation == 'subtract':
        result = Calculator.subtract_numbers(t)
        print(result)
    elif operation == 'multiply':
        result = Calculator.multiply_numbers(t)
        print(result)
    elif operation == 'divide':
        result = Calculator.divide_numbers(t)
        print(result)




