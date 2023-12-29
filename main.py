import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative()])
    calc.print_allowed_chars()

    exp = "4^0.5 * 12 / 7.5 * 0.5"

    print(calc.evaluate_expression(exp))



