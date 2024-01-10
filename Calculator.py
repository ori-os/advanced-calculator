from CalculatorExceptions import OperatorError, CalculatorInputError, CalculationError
from Tree import Tree
from operators.Operator import Operator, Plus, Minus, Multiply, Divide
from operators.OperatorType import OperatorType


def _validate_brackets(expression: str):
    """
    The function gets a mathematical expression as a string and checks whether its valid
    :param expression: The mathematical expression as a string
    :raises CalculatorInputError: if the usages of brackets in the expression is invalid
    """
    order_of_brackets = 0
    for char in expression:
        if order_of_brackets < 0:
            # This means the expression has a bracket closer that comes before its matching bracket opener
            raise CalculatorInputError("Invalid brackets structure: a closing bracket can only come after its "
                                       "matching opening bracket.")
        elif char == '(':
            order_of_brackets += 1
        elif char == ')':
            order_of_brackets -= 1
    # This means the number of openers don't match the number of closers
    if order_of_brackets != 0:
        raise CalculatorInputError("Missing closing bracket(s)", order_of_brackets)


class Calculator:
    def __init__(self):
        self._operators = {}
        self._allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')']

        # Adds the 4 default operations: + - / *
        self.add_operators([Plus(), Minus(), Multiply(), Divide()])

    def add_operator(self, op: Operator):
        """
        Adds a new operator to the calculator
        :param op: The new operator
        :raises InvalidOperatorError:  if the Operator does not exist, has an invalid or a missing attribute.
        :raises CalculatorInputError: if op is not an instance of Operand or if the calculator already has an operator
                 defined under the same symbol
        """
        if op is None:
            raise OperatorError("Operator does not exist. Cannot be None!")
        if not isinstance(op, Operator):
            raise CalculatorInputError("Only objects that are instances of the class Operators can be added to "
                                       "the calculator as an operator")
        if op.get_symbol() is None:
            raise OperatorError("Operator is missing a symbol. Cannot be None!")
        if len(op.get_symbol()) != 1:
            raise OperatorError("Operator symbol must be a single character! Current length",
                                len(op.get_symbol()))
        if op.get_type() is None:
            raise OperatorError("Operator is missing a type. Cannot be None!")
        if op.get_priority() < 1:
            raise OperatorError("Operator has invalid priority set, must be positive! Current priority",
                                op.get_priority())
        if op.get_symbol() in self._allowed_chars:
            raise OperatorError("Operator symbol is already in use and cannot be given an additional use",
                                op.get_symbol())
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
        expression = expression.replace('\t', '')  # Removes all tabs in the expression
        expression = expression.replace('\n', '')  # Removes all newlines in the expression

        # Makes sure the expression isn't empty
        if expression == "":
            raise CalculatorInputError("Expression is empty")

        # Leaving only necessary minuses in the expression
        expression = self._remove_adjacent_minuses(expression)

        # Checks for not supported characters
        self._validate_characters(expression)

        # Checks for valid brackets usage and structure
        _validate_brackets(expression)

        # Checks for a valid expression structure
        self._validate_structure(expression)

        return self._calc(expression)

    def _validate_characters(self, expression: str):
        """
        The function receives a str expression and checks whether it contains illegal characters
        :param expression: A mathematical expression
        :raises CalculatorInputError: if the expression contains characters that the calculator does not support.
        """
        for char in expression:
            if char not in self._allowed_chars:
                raise CalculatorInputError("The expression contains an unsupported character: " + char)

    def _build_expression_tree(self, expression: str) -> Tree:
        """
        The function creates an expression tree of a provided mathematical expression
        :param expression: the mathematical expression
        :return: a new expression tree that represents this expression
        """
        op_index = self._get_last_operator(expression)
        if op_index == -1:
            try:
                return Tree(float(expression))
            except ValueError:
                raise CalculatorInputError("Something went wrong...")
        op = self._get_operator(expression[op_index])
        current_node = Tree(op)

        if op.get_type() != OperatorType.LEFT:
            left_expression = expression[:op_index]
            #  print("LEFT EXPRESSION:", left_expression)
            try:
                left_node = Tree(float(left_expression))
                current_node.set_left(left_node)
            except ValueError:
                if left_expression != '':
                    current_node.set_left(self._build_expression_tree(left_expression))

        if op.get_type() != OperatorType.RIGHT:
            right_expression = expression[op_index + 1:]
            #  print("RIGHT EXPRESSION:", right_expression)
            try:
                right_node = Tree(float(right_expression))
                current_node.set_right(right_node)
            except ValueError:
                if right_expression != '':
                    current_node.set_right(self._build_expression_tree(right_expression))
        return current_node

    def _evaluate_tree(self, tree: Tree) -> float:
        """
        Evaluates the float value of an expression tree
        :param tree: the expression tree
        :return: the value of the expression the tree represents
        :raises CalculationError: if part of the tree cannot be calculated based on the limitations of the
            operators in the tree.
        """
        if tree.is_leaf():
            return tree.get_value()

        op = tree.get_value()
        left_val = None
        if tree.has_left():
            left_val = self._evaluate_tree(tree.get_left())
        right_val = None
        if tree.has_right():
            right_val = self._evaluate_tree(tree.get_right())
        return op.calc(left_val, right_val)

    def _calc(self, expression: str) -> float:
        """
        Evaluates the float value of a complex mathematical expression (which contains brackets)
        :param expression: the mathematical expression as a string
        :return: the result of the expression
        :raises CalculatorInputError: if the expression contains empty brackets: ().
        :raises CalculatorInputError: if the expression is missing a closing bracket.
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
                    if j == i + 2:
                        raise CalculatorInputError("Brackets cannot be empty!")
                    new_expression = expression[i:j]  # expression with brackets
                    tmp = new_expression[1:len(new_expression) - 1]  # expression without brackets
                    expression = expression.replace(new_expression, str(self._calc(tmp)))
                else:
                    raise CalculatorInputError("Missing close bracket")
            i += 1

        return self._evaluate_tree(self._build_expression_tree(expression))

    def is_operator(self, char: str) -> bool:
        """
        Checks whether a character is a supported operator in the calculator
        :param char: the charactor / symbol
        :return: True if it's a supported operator, False otherwise
        """
        return self._operators.get(char) is not None

    def _get_last_operator(self, expression: str) -> int:
        """
        Finds the operator with the lowest priority in the expression
        :param expression: the mathematical expression
        :return: the index of the operator with the highest priority, or -1 if there are no operators
        """
        res = -1
        min_priority = None
        for i in range(len(expression)):
            if self.is_operator(expression[i]) and (
                    min_priority is None or self._get_operator(expression[i]).get_priority() <= min_priority):
                op = self._get_operator(expression[i])
                if op.get_symbol() != '-' or (
                        i > 0 and (not self.is_operator(expression[i - 1])
                                   or self._get_operator(expression[i - 1]).get_type() == OperatorType.RIGHT)):
                    """Differentiating between minus that represent sign and - that are operators"""
                    res = i
                    min_priority = self._get_operator(expression[i]).get_priority()
        return res

    def print_allowed_chars(self):
        """Prints all allowed characters the calculator accepts (numbers as well as operations)."""
        print("These are all of the available characters the calculator accepts:", self._allowed_chars)

    def _remove_adjacent_minuses(self, expression: str) -> str:
        """
        Removes all unnecessary large sequences of minuses as follows:
        A sequence of an odd amount of minuses bigger than 1 will be replaced with a single minus (-)
        A sequence of an even amount of minuses bigger than 2 will be replaced with 2 minuses (--)
        A sequence of an even amount of minuses that comes after an operator that is not of type right will be
        completely removed (since there is no need for them, they cancel each other out)
        :param expression: the mathematical expression
        :return: the new modified expression string
        """
        i = 0
        while i < len(expression) - 1:
            if expression[i] == expression[i + 1] == '-':
                j = i + 1
                while j < len(expression) and expression[j] == '-':
                    j += 1

                # Number of minus is uneven
                if (j - i) % 2 == 1:
                    expression = expression[:i] + '-' + expression[j:]
                    i = -1
                # There is an operator before all the minuses, therefore it's a sign minus (unless it's of type right)
                elif ((i == 0 and j != len(expression)) or (i > 0 and self.is_operator(expression[i-1])
                      and self._get_operator(expression[i-1]).get_type() != OperatorType.RIGHT)):
                    expression = expression[:i] + expression[j:]
                    i = -1
                # The first minus is an operator and there's an even amount of minuses, keeping only 2
                elif j > i+2:
                    expression = expression[:i] + '--' + expression[j:]
                    i = -1

            i += 1
        print("expression: " + expression)
        return expression

    def _validate_structure(self, expression: str):
        """
        Checks whether a mathematical expression has a valid structure.
        :param expression: the mathematical expression
        :raises: CalculatorInputError if the structure of the expression is invalid.
        """
        ch = 0
        while ch < len(expression):

            if expression[ch] == '.':
                """The . symbol must have digits on both of its sides"""
                if ch == 0 or not expression[ch - 1].isnumeric():
                    raise CalculatorInputError(
                        "Invalid expression structure: a decimal point must be part of a number!")
                if ch == len(expression) - 1 or not expression[ch + 1].isnumeric():
                    raise CalculatorInputError(
                        "Invalid expression structure: a decimal point must be part of a number!")

            elif self.is_operator(expression[ch]):
                op = self._get_operator(expression[ch])
                if op.get_type() != OperatorType.LEFT:
                    """The function will raise an exception if:
                        1. The current operator is at the start of the expression, other than minus followed by a number
                            reason: since there is not an operand to the left of the operator
                                exception:
                                    - if the operator is a minus followed by a number/nothing (for expressions like -5)
                            example: +4
                        2. The operator has another operator to its right that is not a right operator 
                            and that the current operator is not a minus.
                            reason: two operators cannot come right after another
                                exception:
                                    - if the current operator is a minus (to account for expressions like 5+-6)
                                    - if the other operator is of type left (to account for expressions like 5!+1)
                            example: 5++1
                    """
                    if ((ch == 0 and (op.get_symbol() != '-' or len(expression) == 1 or not expression[1].isnumeric()))
                            or (ch != 0 and self.is_operator(expression[ch - 1])
                                and op.get_symbol() != '-'
                                and self._get_operator(expression[ch - 1]).get_type() != OperatorType.RIGHT)):
                        raise CalculatorInputError("Invalid expression structure: operator " + op.get_symbol() +
                                                   " is missing an operand to its left")
                if op.get_type() != OperatorType.RIGHT:
                    """The function will raise an exception if:
                        1. The current operator is at the end of the expression.
                            reason: since there is not an operand to the right of the operator
                            example: 4+
                        2. The char after the operator is also an operator that is not a minus or a left operator.
                            reason: two operators cannot come right after another. 
                                    exception: 
                                        - if the 2nd operator is a minus (to account for expressions like 3+-5)
                                        - if the 2nd operator is of type left (to account for expressions like 3+!6)
                            example: 6++1
                        3. The char after the operator is a minus and the char after the minus is not a number
                            reason: to make sure if the operator is followed by a minus, that minus is representing 
                                    a sign rather than an actual operator.
                            example: 3+--5
                            
                        4. The operator is of type left and is followed by another operator
                            reason: since the stacking of ~ is not allowed. 
                            exceptions: if the the other operator is a minus (and therefore can be a sign minus)
                            example: ~~6
                            """
                    if (ch == len(expression) - 1
                            or (self.is_operator(expression[ch + 1])
                                and self._get_operator(expression[ch + 1]).get_symbol() != '-'
                                and ((self._get_operator(expression[ch + 1]).get_type() != OperatorType.LEFT)
                                     or (ch == len(expression) - 2 or (self.is_operator(expression[ch + 2])
                                                                       and expression[ch+2] != '-'))))):
                        raise CalculatorInputError("Invalid expression structure: operator " + op.get_symbol() +
                                                   " is missing an operand to its right")
                    elif (op.get_type() == OperatorType.LEFT
                          and self.is_operator(expression[ch + 1])
                          and (expression[ch + 1] != '-' or ch == len(expression) - 2 or self.is_operator(expression[ch+2]))):
                        raise CalculatorInputError("Invalid expression structure: "
                                                   + op.get_symbol() + " must be followed by a number")

            ch += 1

    def _get_operator(self, symbol: str) -> Operator | None:
        """
        Gets an operator the calculator has based on its symbol
        :param symbol: of the operator
        :return: an instance of an operator which is represented by that matching symbol, or None if no matching
                operator exists in the calculator
        """
        if not self.is_operator(symbol):
            return None
        return self._operators[symbol]

    def evaluate_expression_from_input(self):
        """
        Scans a mathematical expression from the console. Prints its result or an error to console
        """
        s = input("Enter a mathematical expression: \n")

        try:
            print("The result of the expression is: " + str(self.evaluate_expression(s)))
        except (CalculationError, CalculatorInputError) as e:
            print("Could not evaluate the expression: " + str(e))
