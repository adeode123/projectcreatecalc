"""created History class"""


class History:
    history = []

    # pylint: disable=too-few-public-methods
    def append_calculation(calculation):
        """ append function to add calculations"""
        return History.history.append(calculation)
