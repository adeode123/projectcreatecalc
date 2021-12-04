from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """Created child class Addition"""
    def get_result(self):
        result = 0.0
        for float_v in self.values:
            result = result + float_v
        return result
