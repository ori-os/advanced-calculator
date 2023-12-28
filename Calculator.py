from CalculatorExceptions import InvalidOperatorError, CalculatorInputError
from Tree import Tree
from operators.Operator import Operator
from operators.OperatorType import OperatorType


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
            return True
        elif char == '(':
            order_of_brackets += 1
        elif char == ')':
            order_of_brackets -= 1
    # This means the number of openers don't match the number of closers
    if order_of_brackets != 0:
        return True
    return False


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
        expression = self._remove_adjacent_minuses(expression)
        if self._is_expression_valid(expression):
            return self._calc(expression)

        else:
            # TODO
            print("invalid")

        return 0

    def _is_expression_valid(self, expression: str) -> bool:

        if self.has_invalid_characters(expression):
            pass  # TODO: expression contains illegal characters
            return False
        if has_invalid_brackets(expression):
            pass  # TODO: the expression has invalid usages of brackets
            return False
        return True

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

    def _create_expression_tree(self, expression: str) -> Tree:
        op_index = self._get_top_priority(expression)
        #  if op_index == -1:
        #      raise CalculatorInputError("Something went wrong...")
        op = self._operators.get(expression[op_index])
        current_node = Tree(op.get_symbol())

        if op.get_type() != OperatorType.LEFT:
            left_expression = expression[:op_index]
            print("LEFT EXPRESSION:", left_expression)
            try:
                left_node = Tree(float(left_expression))
                current_node.set_left(left_node)
            except ValueError:
                if left_expression != '':
                    current_node.set_left(self._create_expression_tree(left_expression))

        if op.get_type() != OperatorType.LEFT:
            right_expression = expression[op_index+1:]
            print("RIGHT EXPRESSION:", right_expression)
            try:
                right_node = Tree(float(right_expression))
                current_node.set_right(right_node)
            except ValueError:
                if right_expression != '':
                    current_node.set_right(self._create_expression_tree(right_expression))
        return current_node

    def _calc(self, expression: str) -> float:
        """
        Evaluates the float value of an expression
        :param expression: the mathematical expression as a string
        :return: the result of the expression
        :raises CalculatorInputError: if the expression contains empty brackets: ()
        :raises CalculatorInputError: if the expression is missing a closing bracket. Note that this function is called
                after validation meaning this error should never be thrown for this reason. _is_expression_valid() is
                checking for this kind of invalid error
        """
        i = 0
        while i < len(expression):
            if expression[i] == '(':
                """If the current expression has another expression inside brackets in it, the function will evaluate 
                the expression inside the brackets first and replace in the original expression with its evaluation. 
                This is done recursively meaning if the bracketed expression also has a bracketed expression in it it 
                will do the same steps again."""
                brackets_level = 1
                j = i + 1
                while j < len(expression) and brackets_level > 0:
                    if expression[j] == '(':
                        brackets_level += 1
                    elif expression[j] == ')':
                        brackets_level -= 1
                    j += 1
                if brackets_level == 0:
                    if j == i + 1:
                        raise CalculatorInputError("Brackets cannot be empty!")
                    new_expression = expression[i:j]  # expression with brackets
                    tmp = new_expression[1:len(new_expression) - 1]  # expression without brackets
                    expression = expression.replace(new_expression, str(self._calc(tmp)))
                else:
                    raise CalculatorInputError("Missing close bracket")
            i += 1

        temp = self._create_expression_tree(expression)
        # print_tree(temp)
        return self._evaluate_tree(temp)

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
                while j < len(priority) and op.get_priority() >= self._operators.get(
                        expression[priority[j]]).get_priority():
                    j += 1

                if j < len(priority):
                    priority.insert(j, i)
                else:
                    priority.append(i)

        return priority

    def _get_top_priority(self, expression: str) -> int:
        """
        Finds the operator with the highest priority in the expression
        :param expression: the mathematical expression
        :return: the index of the operator with the highest priority, or -1 if there are no operators
        """
        res = -1
        max_priority = 0
        for i in range(len(expression)):
            if self.is_operator(expression[i]) and self._operators[expression[i]].get_priority() > max_priority:
                res = i
                max_priority = self._operators[expression[i]].get_priority()
        return res

    def print_allowed_chars(self):
        """Prints all allowed characters the calculator accepts (numbers as well as operations)."""
        print("These are all of the available characters the calculator accepts:", self._allowed_chars)

    def _remove_adjacent_minuses(self, expression: str) -> str:

        i = 0
        while i < len(expression) - 2:
            if expression[i] == expression[i + 1] == expression[i + 2] == '-':
                j = i + 2
                while j < len(expression) and expression[j] == '-':
                    j += 1

                expression = expression.replace('-' * (j - i), '-' + '-' * (1 - (j - i) % 2))
                return self._remove_adjacent_minuses(expression)
            i += 1
        return expression

    def _get_left_operand(self, expression: str, operator_index: int) -> float:
        if operator_index == 0:
            msg = "The operation " + expression[operator_index] + "is missing a left operand"
            raise CalculatorInputError(msg)

        i = operator_index - 1
        count = 1
        while i > 0 and self._operators.get(expression[i]) is None:
            i -= 1
            count += 1
        if i >= 0 and self._operators.get(expression[i]) == '-':  # number might be negative
            if i == 0 or self.is_operator(expression[i - 1]):
                # if the minus has an operator right before it then its part of the number
                i += 1
        number = expression[operator_index - count:operator_index]
        return float(number)

    def _get_right_operand(self, expression: str, operator_index: int) -> float:
        if operator_index == len(expression) - 1:
            msg = "The operation " + expression[operator_index] + "is missing a right operand"
            raise CalculatorInputError(msg)

        i = operator_index + 1
        count = 1
        if expression[i] == '-':
            count += 1
            i += 1
        while i < len(expression) and self._operators.get(expression[i]) is None:
            i += 1
            count += 1

        number = expression[operator_index + 1:operator_index + count]
        return float(number)

    def _evaluate_tree(self, tree: Tree) -> float:
        if tree.is_leaf():
            return tree.get_value()

        op = self._operators[tree.get_value()]
        left_val = None
        if tree.has_left():
            left_val = self._evaluate_tree(tree.get_left())
        right_val = None
        if tree.has_right():
            right_val = self._evaluate_tree(tree.get_right())
        return op.calc(left_val, right_val)
