import pytest

import Calculator
from CalculatorExceptions import CalculatorInputError
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative

calc = Calculator.Calculator()
calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative()])


def test_1():
    expression = "5-+4"
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression(expression)


def test_2():
    expression = "5^*2"
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression(expression)


def test_3():
    expression = "!6"
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression(expression)


def test_4():
    expression = "5+ ~~6"
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression(expression)


def test_5():
    expression = "8-/4"
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression(expression)
