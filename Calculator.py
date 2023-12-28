from CalculatorExceptions import InvalidOperatorError, CalculatorInputError
from operators.Operator import Operator


def has_invalid_brackets(expression: str) -> bool:
    """
    The function gets a mathematical expression as a string and checks whether its valid
    :param expression: The mathematical expression as a string
    :return: True if the usages of brackets in the expression is invalid, False otherwise
    """
    order_of_brackets = 0
    for char in expression:
        if order_of_brackets < 0:
            # This means the expression has a bracket closer that comes before its matching bracket opener
            return False
        elif char == '(':
            order_of_brackets += 1
        elif char == ')':
            order_of_brackets -= 1
    # This means the number of openers don't match the number of closers
    if order_of_brackets != 0:
        return False
    return True


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
        self._check_invalid_expression(expression)

        """The idea here is to get to a point where the expression contains no brackets - if an expression has 
        brackets, the expression inside the brackets should be evaluated separately (recursively) and have the 
        result of the evaluation inserted to this expression making it a simple number"""

        print(self._create_priority_list(expression))
        return 0

    def _check_invalid_expression(self, expression: str):

        if self.has_invalid_characters(expression):
            pass  # TODO: expression contains illegal characters
        if has_invalid_brackets(expression):
            pass  # TODO: the expression has invalid usages of brackets

        return 0

    def has_invalid_characters(self, expression: str) -> bool:
        """
        The function receives a str expression and checks whether it contains illegal characters
        :param expression: A mathematical expression
        :return: True if the expression contains characters that the calculator does not support, False otherwise.
        """
        for char in expression:
            if char not in self._allowed_chars:
                return True
        return False

    def is_operator(self, char: str) -> bool:
        """
        Checks whether a character is a supported operator in the calculator
        :param char: the charactor / symbol
        :return: True if it's a supported operator, False otherwise
        """
        return self._operators.get(char) is not None

    def _create_priority_list(self, expression: str) -> list:
        """
        Creates a list of all indexes in the expression that are operators. The list will be sorted by the operator's
        priority in the expression.
        Note: This does *not* include brackets
        :param expression: The mathematical expression that needs to be evaluated
        :return: the list of indexes
        """
        priority = []
        for i in range(len(expression)):
            if self.is_operator(expression[i]):
                op = self._operators.get(expression[i])

                j = 0
                while j < len(priority) and op.get_priority() <= self._operators.get(
                        expression[priority[j]]).get_priority():
                    """Checks to see whether the priority of the current operator is greater than the priority of the 
                    Operator in the index j in the priority list. If it is, its getting added to the list before it, 
                    otherwise it will get added to the end of the priority list. By doing so, we end up having a list 
                    of all the indexes of all the operators in the expression in a sorted list in a descending order. 
                    The function goes over every character in the list once meaning the run-time complexity of this 
                    method is O(n) while n is the number of characters in the expression"""
                    j += 1

                if j < len(priority):
                    priority.insert(j, i)
                else:
                    priority.append(i)

        return priority

    def print_allowed_chars(self):
        """Prints all allowed characters the calculator accepts (numbers as well as operations)."""
        print("These are all of the available characters the calculator accepts:", self._allowed_chars)
