import pytest

import Calculator
from CalculatorExceptions import CalculationError
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative, Modulo

calc = Calculator.Calculator()
calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative(), Modulo()])


def test_plus():
    assert calc.evaluate_expression("5+6") == 11


def test_minus():
    assert calc.evaluate_expression("5-6") == -1


def test_multiply():
    assert calc.evaluate_expression("7*10") == 70


def test_divide():
    assert calc.evaluate_expression("12/3") == 4


def test_power():
    assert calc.evaluate_expression("2^4") == 16


def test_factorial_1():
    assert calc.evaluate_expression("5!") == 120


def test_factorial_2():
    with pytest.raises(CalculationError):
        calc.evaluate_expression("-5!")


def test_minimum():
    assert calc.evaluate_expression("2&200") == 2


def test_maximum():
    assert calc.evaluate_expression("2$200") == 200


def test_average():
    assert calc.evaluate_expression("100@200") == 150


def test_modulo():
    assert calc.evaluate_expression("13%3") == 1


def test_negative():
    assert calc.evaluate_expression("~10") == -10
