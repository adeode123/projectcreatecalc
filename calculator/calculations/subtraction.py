from calculator.calculations.calculation import Calculation


class Subtraction(Calculation):
    """Created child class Subtraction"""
    def get_result(self):
        result = 0.0
        for v in self.values:
            result = result - v
        return result
