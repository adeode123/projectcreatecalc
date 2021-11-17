""" Calculator """


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

    def __init__(self, values):
        super().__init__(self)
        self.values = values

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = list(tuple_args)
        return cls(values)

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
        if operation == 'add':
            add_object = Add.create(*self.values)
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

    @classmethod
    def create(cls, *tuple_args: tuple):
        """ create factory class method """
        values = list(tuple_args)
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
        values = list(tuple_args)
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
        values = list(tuple_args)
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
        values = list(tuple_args)
        return cls(values)

    def divide(self):
        """ Divide from child class """
        try:
            result = 1
            for value in self.values:
                result = result / value
            return result
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            return None
