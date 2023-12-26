import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    operators = [Plus(), Minus(), Multiply(), Divide()]
    calc.add_operators(operators)
    calc.print_allowed_chars()