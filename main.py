import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Power(), Factorial(), Negative(), Minimum(), Maximum(), Average()])
    calc.print_allowed_chars()
    print(calc.evaluate_expression("4 * 5 + 1"))
