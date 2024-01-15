import Calculator
from operators.Operator import Power, Factorial, Minimum, Maximum, Average, Negative, Modulo, DigitSum

calc = Calculator.Calculator()
calc.add_operators([Power(), Factorial(), Minimum(), Maximum(), Average(), Negative(), Modulo(), DigitSum()])


def test_1():
    assert calc.evaluate_expression("2^3 * 3! - -4 + (40-20+1) / (3$1)") == 59


def test_2():
    assert calc.evaluate_expression("~-3! / 3 + 10@0 + (10 - (500/100 +1))^2") == 23


def test_3():
    assert calc.evaluate_expression("7----------\t----\n----------------1 + ~8 + 0&(4^4 + 7)") == 0


def test_4():
    assert calc.evaluate_expression("12%11 + 40/((3+ (4+4)/8)^0.5)/10 + ~6") == -3


def test_5():
    assert calc.evaluate_expression("(5+ 1!!!!!!!!) / 3 - ~4 + ((44 + 126@0 - 13)/2 + 13)/20 ") == 9


def test_6():
    assert calc.evaluate_expression("~-3! + (6*6/6) - 4 -- 3 + 15&4 - 4.5/0.5/3") == 12


def test_7():
    assert calc.evaluate_expression("( (5^2 + 5^2) / (~20 + 2 * 29@41) )^-1") == 1


def test_8():
    assert calc.evaluate_expression("10000%5 * 17! + (13/7 * 14)$12 - 20 + 45@12&7^0") == 7


def test_9():
    assert calc.evaluate_expression("(123#%3)! + 4^2 - (8+2)*1.5 - 2 +~11") == -11

