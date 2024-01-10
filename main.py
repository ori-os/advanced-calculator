import Calculator
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative, Modulo, DigitSum

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative(), Modulo(), DigitSum()])
    calc.print_allowed_chars()

    while True:
        calc.evaluate_expression_from_input()
