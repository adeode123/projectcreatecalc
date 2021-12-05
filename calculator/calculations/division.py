"""created module"""
from calculator.calculations.calculation import Calculation

"""Created child class Division"""


class Division(Calculation):

    # pylint: disable=too-few-public-methods
    def get_result(self):
        result = 0.0
        try:
            for float_v in self.values:
                result = result / float_v
            return result
        except ZeroDivisionError:
            print("This is an error")
            return None
