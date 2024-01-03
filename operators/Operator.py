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
    def _calc(self, op1: float = None, op2: float = None) -> float:
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
    def _calc(self, op1: float = None, op2: float = None) -> float:
        return op1 - op2

    def get_symbol(self) -> str:
        return '-'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Multiply(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        return op1 * op2

    def get_symbol(self) -> str:
        return '*'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Divide(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        if op2 == 0:
            raise CalculationError("Cannot divide by 0")
        return op1 / op2

    def get_symbol(self) -> str:
        return '/'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Power(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        if op1 < 0 and op2 < 1:
            raise CalculationError("Cannot calculate the root of a negative number")
        if op1 == 0 and op2 == 0:
            raise CalculationError("Cannot calculate 0 to the power of 0")
        return op1 ** op2

    def get_symbol(self) -> str:
        return '^'

    def get_priority(self) -> int:
        return 3

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Modulo(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        return op1 % op2

    def get_symbol(self) -> str:
        return '%'

    def get_priority(self) -> int:
        return 4

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Average(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        return (op1 + op2) / 2

    def get_symbol(self) -> str:
        return '@'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minimum(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        if op1 < op2:
            return op1
        return op2

    def get_symbol(self) -> str:
        return '&'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Maximum(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        if op1 > op2:
            return op1
        return op2

    def get_symbol(self) -> str:
        return '$'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Negative(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        return -op2

    def get_symbol(self) -> str:
        return '~'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.LEFT


class Factorial(Operator):
    def _calc(self, op1: float = None, op2: float = None) -> float:
        if op1 < 0:
            raise CalculationError("Can not calculate the factorial of a negative number!")
        op = int(op1)
        if op != op1:
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
