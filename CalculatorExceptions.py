class InvalidOperatorError(Exception):
    def __init__(self, reason: str, value=None):
        if value is not None:
            reason += ": " + str(value)
        super().__init__(reason)


class CalculatorInputError(Exception):
    def __init__(self, reason: str, value: int = None):
        if value is not None:
            reason += ": " + str(value)
        super().__init__(reason)


class CalculationError(Exception):

    def __init__(self, reason :str):
        super().__init__(reason)
