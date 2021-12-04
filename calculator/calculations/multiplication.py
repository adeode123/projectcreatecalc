from calculator.calculations.calculation import Calculation


class Multiplication(Calculation):
    """Created child class Multiply"""
    def get_result(self):
        result = 0.0
        for v in self.values:
            result = result * v
        return result
