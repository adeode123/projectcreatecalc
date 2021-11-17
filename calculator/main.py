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
    def addition(num_1, num_2):
        """ Add """
        return num_1 + num_2

    @staticmethod
    def subtraction(*tuple_args: tuple):
        """ Subtract """
        result = 0
        for arg in tuple_args:
            result = arg - result
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
        if operation == 'add':
            add_object = Add(first_num=self.first_num, second_num=self.second_num)
            result = add_object.add()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": add_object
            })
            return result

        if operation == 'subtract':
            subtract_object = Subtract.create(*self.values)
            result = subtract_object.subtract()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": subtract_object
            })
            return result

        if operation == 'multiply':
            multiply_object = Multiply.create(*self.values)
            result = multiply_object.multiply()
            Calculator.add_calculation_to_history({
                "result": result,
                "object": multiply_object
            })
            return result

        if operation == 'divide':
            divide_object = Divide.create(*self.values)
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
        result = 0
        for value in self.values:
            result = value - result
        return result


class Multiply(Calculator):
    """ Multiply inherited from Calculator """

    def multiply(self):
        """ Multiply from child class """
        result = 1
        for value in self.values:
            result = value * result
        return result


class Divide(Calculator):
    """ Divide inherited from Calculator """

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
