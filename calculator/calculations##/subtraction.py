from calculator.calculations.calculation import Calculation


class Subtraction(Calculation):
    """Created child class Subtraction"""
    def get_result(self):
        result = 0.0
        for float_v in self.values:
            result = result - float_v
        return result
