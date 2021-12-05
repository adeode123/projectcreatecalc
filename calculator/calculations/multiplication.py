"""created module"""
from calculator.calculations.calculation import Calculation


class Multiplication(Calculation):
    """Created child class Multiply"""

    # pylint: disable=too-few-public-methods
    def get_result(self):
        """get result"""
        result = 0.0
        for float_v in self.values:
            result = result * float_v
        return result
