from abc import abstractmethod

from OperatorType import OperatorType


class Operator:
    def __init__(self):
        pass

    @abstractmethod
    def calc(self, op1: float, op2: float = None) -> float:
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
    def calc(self, op1: float, op2: float = None) -> float:
        return op1 + op2

    def get_symbol(self) -> str:
        return '+'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minus(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
        return op1 - op2

    def get_symbol(self) -> str:
        return '-'

    def get_priority(self) -> int:
        return 1

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Multiply(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
        return op1 * op2

    def get_symbol(self) -> str:
        return '*'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Divide(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
        return op1 / op2

    def get_symbol(self) -> str:
        return '/'

    def get_priority(self) -> int:
        return 2

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Power(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
        return op1 ** op2

    def get_symbol(self) -> str:
        return '^'

    def get_priority(self) -> int:
        return 3

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Modulo(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
        return op1 % op2

    def get_symbol(self) -> str:
        return '%'

    def get_priority(self) -> int:
        return 4

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Average(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
        return (op1 + op2) / 2

    def get_symbol(self) -> str:
        return '@'

    def get_priority(self) -> int:
        return 5

    def get_type(self) -> OperatorType:
        return OperatorType.INNER


class Minimum(Operator):
    def calc(self, op1: float, op2: float = None) -> float:
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
    def calc(self, op1: float, op2: float = None) -> float:
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
    def calc(self, op1: float, unused: float = None) -> float:
        return -op1

    def get_symbol(self) -> str:
        return '~'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.LEFT


class Factorial(Operator):
    def calc(self, op1: float, unused: float = None) -> float:
        op = int(op1)
        result = 1
        for i in range (1,op+1):
            result *= i
        return result

    def get_symbol(self) -> str:
        return '!'

    def get_priority(self) -> int:
        return 6

    def get_type(self) -> OperatorType:
        return OperatorType.RIGHT
