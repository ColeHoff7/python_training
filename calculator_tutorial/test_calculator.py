from calculator import Calculator

calc = Calculator()

def test_add_success():
    res = calc.add(1,4)
    assert res == 5

def test_subtract_success():
    res = calc.subtract(3, 9)
    assert res == -6

def test_multiply_success():
    res = calc.multiply(3,3)
    assert res == 9

def test_divide_success():
    res = calc.divide(15,5)
    assert res == 3

def test_add_multiple_success():
    res = calc.add_multiple(1,2,3)
    assert res == 6

