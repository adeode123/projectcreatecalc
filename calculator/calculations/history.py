class History:

    """created History class"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def append_calculation(calculation):
        """ append function to add calculations"""
        return History.history.append(calculation)

