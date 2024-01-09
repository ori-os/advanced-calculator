from abc import abstractmethod

from CalculatorExceptions import CalculationError
from operators.OperatorType import OperatorType


class Operator:
    """
    This Class is an abstract class for calculator operators. If you are interested to add a new operation to your
    calculator, you may extend (inherit) from this class and complete the abstract methods to create a brand-new
    operator!
    """

    def __init__(self):
        pass

    def calc(self, left_operand: float = None, right_operand: float = None) -> float:
        if self.get_type() == OperatorType.INNER:
            if left_operand is None or right_operand is None:
                pass  # TODO raise exception
        elif self.get_type() == OperatorType.LEFT:
            if left_operand is None:
                pass  # TODO raise exception
        elif self.get_type() == OperatorType.RIGHT:
            if right_operand is None:
                pass  # TODO raise exception
        return self._calc(left_operand, right_operand)

    @abstractmethod
    def _calc(self, left: float = None, right: float = None) -> float:
        pass

    @abstractmethod
    def get_symbol(self) -> str:
        pass

    @abstractmethod
    def get_priority(self) -> int:
        pass

    @abstractmethod
    def get_type(self) -> OperatorType:
        pass


class Plus(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
        return left + right

    def get_symbol(self) -> str:
        return '+'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minus(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
        return left - right

    def get_symbol(self) -> str:
        return '-'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Multiply(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
        return left * right

    def get_symbol(self) -> str:
        return '*'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Divide(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
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
    def _calc(self, left: float = None, right: float = None) -> float:
        if left < 0 and right < 1:
            raise CalculationError("Cannot calculate the root of a negative number")
        if left == 0 and right == 0:
            raise CalculationError("Cannot calculate 0 to the power of 0")
        return left ** right

    def get_symbol(self) -> str:
        return '^'

    def get_priority(self) -> int:
        return 3

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Modulo(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
        return left % right

    def get_symbol(self) -> str:
        return '%'

    def get_priority(self) -> int:
        return 4

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Average(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
        return (left + right) / 2

    def get_symbol(self) -> str:
        return '@'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minimum(Operator):
    def _calc(self, left: float = None, right: float = None) -> float:
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
    def _calc(self, left: float = None, right: float = None) -> float:
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
    def _calc(self, unused: float = None, right: float = None) -> float:
        return -right

    def get_symbol(self) -> str:
        return '~'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.LEFT


class Factorial(Operator):
    def _calc(self, left: float = None, unused: float = None) -> float:
        if left < 0:
            raise CalculationError("Can not calculate the factorial of a negative number!")
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
    def _calc(self, left: float = None, unused: float = None) -> float:

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
