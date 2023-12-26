from operators.Operator import Operator


class Calculator:
    def __init__(self):
        self._operators = {}
        self._allowed_chars = "0123456789.()"

    def add_operator(self, op: Operator):
        if op is None:
            pass  # TODO: raise an exception - no operator provided!
        if op.get_symbol() is None:
            pass  # TODO: raise an exception - operation symbol doesn't exist!
        if len(op.get_symbol()) != 1:
            pass  # TODO: raise an exception - operation symbol is invalid - must be exactly 1 character!
        if op.get_type() is None:
            pass  # TODO: raise an exception - operator type was not assigned!
        if op.get_priority() < 1:
            pass  # TODO: raise an exception - invalid priority set, must be positive!
        if self._operators.get(op.get_symbol()) is not None:
            pass  # TODO: raise an exception - operation of that symbol is already defined
        self._operators[op.get_symbol()] = op
        self._allowed_chars += op.get_symbol()

    def add_operators(self, operators: list):
        for op in operators:
            if not isinstance(op, Operator):
                pass  # TODO: raise exception
            self.add_operator(op)

    def evaluate_expression(self, expression: str):
        pass  # TODO

    def print_allowed_chars(self):
        print("These are all of the available characters the calculator accepts:", self._allowed_chars)
