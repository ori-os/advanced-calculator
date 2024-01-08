import pytest

import Calculator
from CalculatorExceptions import CalculatorInputError
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative, Modulo

calc = Calculator.Calculator()
calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative(), Modulo()])


def test_syntax_1():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("5-+4")


def test_syntax_2():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("5^*2")


def test_syntax_3():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("!6")


def test_4():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("5+ ~~6")


def test_5():
    with pytest.raises(CalculatorInputError):
        calc.evaluate_expression("8-/4")
