from CalculatorExceptions import InvalidOperatorError, CalculatorInputError
from operators.Operator import Operator


class Calculator:
    def __init__(self):
        self._operators = {}
        self._allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')']

    def add_operator(self, op: Operator):
        """
        Adds a new operator to the calculator
        :param op: The new operator
        :raises InvalidOperatorError:  if the Operator does not exist, has an invalid or a missing attribute.
        :raises CalculatorInputError: if op is not an instance of Operand or if the calculator already has an operator
                 defined under the same symbol
        """
        if op is None:
            raise InvalidOperatorError("Operator does not exist. Cannot be None!")
        if not isinstance(op, Operator):
            raise CalculatorInputError("Only objects that are instances of the class Operators can be added to "
                                       "the calculator as an operator")
        if op.get_symbol() is None:
            raise InvalidOperatorError("Operator is missing a symbol. Cannot be None!")
        if len(op.get_symbol()) != 1:
            raise InvalidOperatorError("Operator symbol must be a single character! Current length",
                                       len(op.get_symbol()))
        if op.get_type() is None:
            raise InvalidOperatorError("Operator is missing a type. Cannot be None!")
        if op.get_priority() < 1:
            raise InvalidOperatorError("Operator has invalid priority set, must be positive! Current priority",
                                       op.get_priority())
        if self._operators.get(op.get_symbol()) is not None:
            raise CalculatorInputError("You can't add multiple operators that use same symbol in the same calculator")
        self._operators[op.get_symbol()] = op
        self._allowed_chars.append(op.get_symbol())

    def add_operators(self, operators: list):
        """
             Adds new operators to the calculator
             :param operators: A list of the new operators
             :raises InvalidOperatorError: if an Operator does not exist, has an invalid or a missing attribute.
             :raises CalculatorInputError: if op is not an instance of Operand or if the calculator already has an
             operator defined under the same symbol.
             """
        for op in operators:
            self.add_operator(op)

    def evaluate_expression(self, expression: str) -> float:
        expression = expression.replace(' ', '')  # Removes all spaces in the expression
        try:
            self._check_invalid_characters(expression)
        except CalculatorInputError:
            pass  # TODO - expression contains illegal characters
        print(expression)
        return 0

    def _check_invalid_characters(self, expression: str):
        """
        The function receives a str expression and checks whether it contains illegal characters
        :param expression: A mathematical expression
        :raises CalculatorInputError: if the given expression contains not supported characters / operations
        """
        for char in expression:
            if char not in self._allowed_chars:
                raise CalculatorInputError("Expression contains invalid characters")

    def print_allowed_chars(self):
        """Prints all allowed characters the calculator accepts (numbers as well as operations)."""
        print("These are all of the available characters the calculator accepts:", self._allowed_chars)
