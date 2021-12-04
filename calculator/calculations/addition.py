from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """Created child class Addition"""
    def get_result(self):
        result = 0.0
        for number in self.values:
            result = result + number
        return result
