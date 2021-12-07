"""created new module"""


class History:

    """created History class"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def append_calculation(calculation):
        """ append function to add calculations"""
        return History.history.append(calculation)

    @staticmethod
    def clear_history():
        """clears history"""
        History.history.clear()
        return True

    @staticmethod
    def count_history():
        """returns number of items in the history"""
        return len(History.history)

    @staticmethod
    def get_last_calculation():
        """gets last calculation"""
        return History.history[-1]

    @staticmethod
    def get_first_calculation():
        """gets the first calculation"""
        return History.history[0]

    @staticmethod
    def get_calculation(index):
        """returns specific calculations from history"""
        return History.history[index]
