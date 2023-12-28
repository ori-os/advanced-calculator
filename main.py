import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Plus(), Minus(), Multiply(), Divide(), Power()])
    calc.print_allowed_chars()
    calc.evaluate_expression("2 + (-----3 * ------ 3) / ( 8 -- 7 / (9 ----------- 1))")

