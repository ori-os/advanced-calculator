import Calculator
from CalculatorExceptions import CalculatorInputError, CalculationError
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative, Modulo

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative(), Modulo()])
    calc.print_allowed_chars()

    while True:
        s = input("Enter a mathematical expression: \n")

        try:
            print("The result of the expression is: " + str(calc.evaluate_expression(s)))
        except (CalculationError, CalculatorInputError) as e:
            print("Could not evaluate the expression: " + str(e))
