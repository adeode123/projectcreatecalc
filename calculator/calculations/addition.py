from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """Created child class Addition"""

    def get_result(self):
        """gets result"""
        result = 0.0
        for v in self.values:
            result = result + v
        return result
