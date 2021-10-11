from math_series import __version__
from math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

"""
*Fabonacci
===========
test cases: 
    -1 => "Input is not valid
    "4" => "Input is not valid
    0 => 0
    1 => 1
    9 => 34   
"""
def test_fabonacci_0():
    expected =0
    actual=fibonacci(0)
    assert expected==actual

