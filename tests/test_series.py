from math_series import __version__
from math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

"""
*Fabonacci
===========
test cases: 
    -1 => "The value must be positive"
    "4" => "The value must be intager"
    0 => 0
    1 => 1
    9 => 34   
"""
def test_fabonacci_0():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_fabonacci_1():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_fabonacci_9():
    expected = 34
    actual = fibonacci(9)
    assert expected == actual

def test_fabonacci_negative():
    expected = "The value must be positive"
    actual = fibonacci(-1)
    assert expected == actual

def test_fabonacci_string():
    expected = "The value must be intager"
    actual = fibonacci('4')
    assert expected == actual


"""
*Lucas
===========
test cases: 
    -1 => "The value must be positive"
    "4" => "The value must be intager"
    0 => 2
    1 => 1
    6 => 18  
"""

def test_lucas_0():
    expected = 2
    actual = lucas(0)
    assert expected == actual

def test_lucas_1():
    expected = 1
    actual = lucas(1)
    assert expected == actual

def test_lucas_6():
    expected = 18
    actual = lucas(6)
    assert expected == actual

def test_lucas_negative():
    expected = "The value must be positive"
    actual = lucas(-1)
    assert expected == actual

def test_lucas_string():
    expected = "The value must be intager"
    actual = lucas('4')
    assert expected == actual