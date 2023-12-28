import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Plus(), Minus(), Multiply(), Divide(), Power()])
    calc.print_allowed_chars()
    print(calc.evaluate_expression("5^4"))

