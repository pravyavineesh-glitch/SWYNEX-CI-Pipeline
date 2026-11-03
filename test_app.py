from app import add_numbers, multiply_numbers, subtract_numbers


def test_add_numbers():
    assert add_numbers(10,20) == 30

def test_add_numbers_with_zero():
    assert add_numbers(0,10) == 10

def test_subtract_numbers():
    assert subtract_numbers(10,20) == -10

def test_subtract_numbers_with_zero():
    assert subtract_numbers(10,0) == 10

def test_subtract_numbers_with_zero_begin():
    assert subtract_numbers(0,20) == -20

def test_multiply_numbers():
    assert multiply_numbers(10,20) == 200

def test_multiply_numbers_with_zero():
    assert multiply_numbers(10,0) == 0