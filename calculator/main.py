""" Calculator """

import pandas as pd
import time

class Calculation:
    """ Abstract base class for Calculations"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values):
        self.values = values

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """


class Calculator(Calculation):
    """ Calculator class """
    calculator_history = []
    history_log_file = r"C:\Users\Abosede\PycharmProjects\calc_part2\calculator\history.csv"

    def __init__(self, values):
        super().__init__(self)
        self.raw_values = values
        self.values = list(values)

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        # values = list(tuple_args)
        return cls(tuple_args)

    @staticmethod
    def get_history():
        """ History of calculator operations"""
        return Calculator.calculator_history

    @staticmethod
    def get_last_calculation():
        """ Get last calculation"""
        return Calculator.calculator_history[-1]

    @staticmethod
    def get_first_calculation():
        """ Get first calculation"""
        return Calculator.calculator_history[0]

    @staticmethod
    def add_calculation_to_history(record):
        """ Add calculation to calculation history """
        Calculator.calculator_history.append(record)
        return Calculator.calculator_history

    @staticmethod
    def get_last_calculation_result():
        """ Get last calculation result """
        return Calculator.calculator_history[-1].get("result", None)

    @staticmethod
    def get_last_calculation_object():
        """ Get last calculation object """
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
    def get_history_from_csv():
        """Read the history from csv and put it into the history """
        try:
            df = pd.read_csv(Calculator.history_log_file)
            Calculator.calculator_history = df.values.tolist()
        except FileNotFoundError:
            print("No history exists for this session")

    @staticmethod
    def write_history_to_csv():
        """Write the history to csv file"""
        df = pd.DataFrame.from_dict({"row_1": Calculator.get_last_calculation()}, orient="index")
        df.to_csv(Calculator.history_log_file, mode="a", header=False, index=False)
        return None

    @staticmethod
    def addition(*tuple_args: tuple):
        """ Add """
        result = 0
        for arg in tuple_args:
            result = arg + result
        return result

    @staticmethod
    def subtraction(*tuple_args: tuple):
        """ Subtract """
        result = 0
        values = list(tuple_args)
        for val in values:
            result = val - result
        return result

    @staticmethod
    def multiplication(*tuple_args: tuple):
        """ Multiplication """
        result = 1
        values = list(tuple_args)
        for val in values:
            result = val * result
        return result

    @staticmethod
    def division(*tuple_args: tuple):
        """ Division """
        try:
            result = 1
            values = list(tuple_args)
            for val in values:
                result = val / result
            return result
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            return None

    def factory(self, operation):
        """ Factory helper method """
        # result = 0

        if operation == 'add':
            add_object = Add.create(*self.values)
            result = add_object.add()

        elif operation == 'subtract':
            subtract_object = Subtract.create(*self.values)
            result = subtract_object.subtract()

        elif operation == 'multiply':
            multiply_object = Multiply.create(*self.values)
            result = multiply_object.multiply()

        elif operation == 'divide':
            divide_object = Divide.create(*self.values)
            result = divide_object.divide()

        else:
            return "Invalid Operation"

        history = {
            "timestamp": str(time.time()),
            "filename": str(Calculator.history_log_file),
            "record_number": str(self.raw_values),
            "operation": operation,
            "result": str(result)
        }
        Calculator.add_calculation_to_history(history)
        return result


class Add(Calculator):
    """ Add inherited from Calculator"""

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = []
        for val in tuple_args:
            values.append(int(val))
        return cls(values)

    def add(self):
        """ Add from child class"""
        result = 0
        for val in self.values:
            result = val + result
        return result


class Subtract(Calculator):
    """ Subtract inherited from Calculator """

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = []
        for val in tuple_args:
            values.append(int(val))
        return cls(values)

    def subtract(self):
        """ Subtract from child class"""
        result = 0
        for value in self.values:
            result = value - result
        return result


class Multiply(Calculator):
    """ Multiply inherited from Calculator """

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = []
        for val in tuple_args:
            values.append(int(val))
        return cls(values)

    def multiply(self):
        """ Multiply from child class """
        result = 1
        for value in self.values:
            result = value * result
        return result


class Divide(Calculator):
    """ Divide inherited from Calculator """

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = []
        for val in tuple_args:
            values.append(int(val))
        return cls(values)

    def divide(self):
        """ Divide from child class """
        try:
            result = 1
            for value in self.values:
                result = value / result
            return result
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            return None