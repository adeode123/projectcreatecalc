from calculator.calculations.calculation import Calculation


class Multiplication(Calculation):
    """Created child class Multiply"""
    def get_result(self):
        """gets result"""
        result = 0.0
        for float_v in self.values:
            result = result * float_v
        return result
