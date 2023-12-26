import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Plus(), Minus(), Multiply(), Divide()])
    calc.print_allowed_chars()
    calc.evaluate_expression("4 + 4 + 2 / 7 -- 4 --- 3 -------------------- ~6")

