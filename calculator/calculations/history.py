"""created History class"""


class History:
    history = []

    @staticmethod
    def append_calculation(calculation):
        """ append function to add calculations"""
        return History.history.append(calculation)
