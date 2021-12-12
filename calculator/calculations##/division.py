from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """Created child class Division"""
    def get_result(self):
        """GETS RESULT"""
        result = 0.0
        try:
            for float_v in self.values:
                result = result / float_v
            return result
        except ZeroDivisionError:
            print("This is an error")
            return None
        