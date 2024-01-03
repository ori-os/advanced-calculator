from operators.Operator import Operator


class Tree:
    def __init__(self, value: float | Operator, left: 'Tree' = None, right: 'Tree' = None):
        self._left = left
        self._right = right
        self._value = value

    def get_right(self) -> 'Tree':
        return self._right

    def get_left(self) -> 'Tree':
        return self._left

    def set_left(self, left: 'Tree'):
        self._left = left

    def set_right(self, right: 'Tree'):
        self._right = right

    def get_value(self) -> Operator | float:
        return self._value

    def is_leaf(self) -> bool:
        return self._left is None and self._right is None

    def has_left(self) -> bool:
        return self._left is not None

    def has_right(self) -> bool:
        return self._right is not None




