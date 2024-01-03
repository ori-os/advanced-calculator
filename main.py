import Calculator
from CalculatorExceptions import CalculatorInputError, CalculationError
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative

if __name__ == '__main__':
    calc = Calculator.Calculator()
    calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative()])
    calc.print_allowed_chars()

    while True:
        s = input("Enter a mathematical expression: \n")

        try:
            print("The result of the expression is: " + str(calc.evaluate_expression(s)))
        except CalculatorInputError as e:
            print("Could not evaluate the expression: " + str(e))
        except CalculationError as e:
            print("Could not evaluate the expression: " + str(e))



