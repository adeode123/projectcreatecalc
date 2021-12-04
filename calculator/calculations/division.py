from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """Created child class Division"""
    def get_result(self):
        result = 0.0
        try:
            for v in self.values:
                result = result / v
            return result
        except ZeroDivisionError:
            print("This is an error")
            return None
        