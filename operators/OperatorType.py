from enum import Enum


class OperatorType(Enum):
    INNER = 0  # The operator should be between 2 operands, and it applies the operation between the two
    LEFT = 1  # The operator should be to the left of a single operand, and it applies the operation on it
    RIGHT = 2  # The operator should be to the right of a single operand, and it applies the operation on it
