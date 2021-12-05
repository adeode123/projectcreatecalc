"""created module"""
from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """Created child class Addition"""

    # pylint: disable=too-few-public-methods

    def get_result(self):
        """gets result"""
        result = 0.0
        for float_v in self.values:
            result = result + float_v
        return result
