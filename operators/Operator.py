from abc import abstractmethod

from CalculatorExceptions import CalculationError, OperatorError
from operators.OperatorType import OperatorType


class Operator:
    """
    This Class is an abstract class for calculator operators. If you are interested to add a new operation to your
    calculator, you may extend (inherit) from this class and complete the abstract methods to create a brand-new
    operator!
    """

    def __init__(self):
        pass

    def calc(self, left_operand: float | None, right_operand: float | None) -> float:
        """
        Calculates the float value after applying the operation on the operators
        :param left_operand: the operand to the left of the operator, or None if there is no such operand
        :param right_operand: the operand to the right of the operator, or None if there is no such operand
        :raises OperatorError: if the current operator requires left or right operands, and they are None
        :raises CalculationError: if there has been an error while tempting to calculate
        :return: The result of the operation between the operand(s)
        """
        if self.get_type() != OperatorType.LEFT and left_operand is None:
            raise OperatorError("Operator" + self.get_symbol() + " is missing a left operand")
        elif self.get_type() != OperatorType.RIGHT and right_operand is None:
            raise OperatorError("Operator" + self.get_symbol() + " is missing a right operand")
        return self._calc(left_operand, right_operand)

    @abstractmethod
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        An abstract method. All operators that extends this class must implement this method that evaluates the value
        between two operands resulting by the operation it did.
        :param left: The operand to the left of the operator, or None if the operator does not use a left operand
        :param right: The operand to the right of the operator, or None if the operator does not use a left operand
        :raises CalculationError: if there has been an error while tempting to calculate
        :return: the result of the operation
        """
        pass

    @abstractmethod
    def get_symbol(self) -> str:
        """
        Gets the char symbol representing the operator
        :return: the symbol
        """
        pass

    @abstractmethod
    def get_priority(self) -> int:
        """
        Gets the priority of the operator. Operators with higher priority will be evaluated before ones with lower ones.
        :return: the priority of the operator
        """
        pass

    @abstractmethod
    def get_type(self) -> OperatorType:
        """
        Gets the type of the operator:

        INNER: The operator should be between 2 operands, and it applies the operation between the two

        LEFT: The operator should be to the left of a single operand, and it applies the operation on it

        RIGHT: The operator should be to the right of a single operand, and it applies the operation on it

        :return: the type of the operator
        """
        pass


class Plus(Operator):
    """
    Extends the class operator, calculates the sum of 2 operands.
    Symbol: +
    Priority: 1
    Type: INNER
    """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the sum between the left and right operand.
        :param left: the left operand
        :param right: the right operand
        :return: the sum of the two operands
        """
        return left + right

    def get_symbol(self) -> str:
        return '+'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minus(Operator):
    """
     Extends the class operator, calculates the differance between 2 operands.
     Symbol: -
     Priority: 1
     Type: INNER
     """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the difference between the left and right operands
        :param left: the left operand
        :param right: the right operand
        :return: the difference
        """
        return left - right

    def get_symbol(self) -> str:
        return '-'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Multiply(Operator):
    """
        Extends the class operator, calculates the result of multiplication between 2 operands.
        Symbol: *
        Priority: 2
        Type: INNER
        """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the result of multiplication between the left and right operands.
        :param left: the left operand
        :param right: the right operand
        :return: the result of the multiplication
        """
        return left * right

    def get_symbol(self) -> str:
        return '*'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Divide(Operator):
    """
        Extends the class operator, calculates the result of division between 2 operands.
        Symbol: /
        Priority: 2
        Type: INNER
        """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the result of division between the left and right operands.
        :param left: the left operand
        :param right: the right operand
        :raises CalculationError: if the right operand is 0
        :return: the result of the operation
        """
        if right == 0:
            raise CalculationError("Cannot divide by 0")
        return left / right

    def get_symbol(self) -> str:
        return '/'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Power(Operator):
    """
    Extends the class operator, calculates the result of one operand raised to the power of another
        Symbol: ^
        Priority: 3
        Type: INNER
    """
    def _calc(self, base: float | None, exponent: float | None) -> float:
        """
        Calculates the result of the left operand raised to the power of the right operand
        :param base: the left operand
        :param exponent: the right operand
        :raises CalculationError: if the base is negative while the exponent is between -1 and 1
        :raises CalculationError: if both the base and exponent are 0
        :return: the result of the operation
        """
        if base < 0 and -1 < exponent < 1:
            raise CalculationError("Cannot calculate the root of a negative number")
        if base == 0 and exponent == 0:
            raise CalculationError("Cannot calculate 0 to the power of 0")
        return base ** exponent

    def get_symbol(self) -> str:
        return '^'

    def get_priority(self) -> int:
        return 3

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Modulo(Operator):
    """
    Extends the class operator, calculates the remainder of the result of the calculation of division between operands
        Symbol: %
        Priority: 4
        Type: INNER
    """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the remainder of the result of the calculation of division between the left and right operand
        :param left: the one being divided
        :param right: the divider
        :return: the result of the operation
        """
        return left % right

    def get_symbol(self) -> str:
        return '%'

    def get_priority(self) -> int:
        return 4

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Average(Operator):
    """
    Extends the class operator, calculates the average of two operands
        Symbol: @
        Priority: 5
        Type: INNER
    """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the average of the left and right operand
        :param left: the left operand
        :param right: the right operand
        :return: the result of the calculation
        """
        return (left + right) / 2

    def get_symbol(self) -> str:
        return '@'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minimum(Operator):
    """
    Extends the class operator, calculates the minimum between two operands
        Symbol: &
        Priority: 5
        Type: INNER
    """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
        Calculates the minimum value between the left and right operands
        :param left: the left operand
        :param right: the right operand
        :return: the result of the operation
        """
        if left < right:
            return left
        return right

    def get_symbol(self) -> str:
        return '&'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Maximum(Operator):
    """
    Extends the class operator, calculates the maximum between two operands
        Symbol: $
        Priority: 5
        Type: INNER
    """
    def _calc(self, left: float | None, right: float | None) -> float:
        """
         Calculates the maximum value between the left and right operands
        :param left: the left operand
        :param right: the right operand
        :return: the result of the operation
        """
        if left > right:
            return left
        return right

    def get_symbol(self) -> str:
        return '$'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Negative(Operator):
    """
    Extends the class operator, changes the sign of the operand to its right
        Symbol: ~
        Priority: 6
        Type: LEFT
    """
    def _calc(self, unused: float | None, right: float | None) -> float:
        """
        Changes the sign of the operand to its right
        :param unused: not in use, since there is no left operand
        :param right: the right operand
        :return: the right operand with a changed sign
        """
        return -right

    def get_symbol(self) -> str:
        return '~'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.LEFT


class Factorial(Operator):
    """
    Extends the class operator, calculates the factorial of the operand to its left
        Symbol: !
        Priority: 6
        Type: RIGHT
    """
    def _calc(self, left: float | None, unused: float | None) -> float:
        """
        Calculates the factorial of the operand to its left
        :param left: the operator to its left
        :param unused: not in use since there is no right operand
        :raises CalculationError: if the left operator is not an integer
        :return: the result of the operation
        """
        if left < 0:
            return -self._calc(-left, unused)
        op = int(left)
        if op != left:
            raise CalculationError("Can only calculate the factorial of an integer!")
        result = 1
        for i in range(1, op + 1):
            result *= i
        return result

    def get_symbol(self) -> str:
        return '!'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.RIGHT


class DigitSum(Operator):
    """
    Extends the class operator, calculates the sum of the digits of the operator to its left
        Symbol: #
        Priority: 6
        Type: RIGHT
    """
    def _calc(self, left: float | None, unused: float | None) -> float:
        """
        Calculates the sum of the digits of the left operator
        :param left: the left operator
        :param unused: not in use since there is no right operand
        :return: the sum of the digits. If the operator is negative it will return minus the sum of the digits.
        """
        is_neg = left < 0
        left = abs(left)

        while int(left) != left:
            left *= 10

        res = 0
        while left != 0:
            res += left % 10
            left //= 10

        if is_neg:
            res *= -1
        return res

    def get_symbol(self) -> str:
        return '#'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.RIGHT
