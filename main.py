import Calculator
from operators.Operator import *

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative()])
    calc.print_allowed_chars()

    while True:
        s = input("Enter a mathematical expression: \n")
        print(calc.evaluate_expression(s))



