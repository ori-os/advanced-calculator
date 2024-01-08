import pytest

import Calculator
from CalculatorExceptions import CalculatorInputError
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative

calc = Calculator.Calculator()
calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative()])


def test_invalid_characters():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("shalom ani ori blah blah blah")


def test_empty():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("")


def test_whitespaces():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("\n \t")
