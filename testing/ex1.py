
import sys
import pytest

def func1(x, y):
    return x+y

def func2(x, y):
    return x*y

def test_sum():
    assert func1(1, 20) == 21

def test_product():
    assert func2(10,15) == 150

@pytest.mark.parametrize("num1, num2, result", [(20, 0, 0), (10, 10, 100), (1, 5, 5), (10, 2, 20)])
def test_product_params(num1, num2, result):
    assert func2(num1, num2) == result

@pytest.mark.skipif(sys.version_info.major == 3 and sys.version_info.minor == 7, reason='because')
def test_sum2():
    assert func1(5, 6) == 11
