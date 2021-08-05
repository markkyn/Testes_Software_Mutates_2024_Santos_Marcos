import sys
sys.path.insert(0, './deliverable3/src')
from exponential_function import ExponentialFunction
import math

"""
This module contains tests for exponential_function
module and its functions. It includes a set of
unit tests
Two ExponentialFunction objects are created, one to 
get the cube root of 3, and another for the square
root of 2
"""

# Cube root of 3 test
cube_root = ExponentialFunction(0, 0, 0)
cube_root.set_mult_num("1")
cube_root.set_base_num("3")
cube_root.set_exp_num("1/3")

# Square root of 2 test
square_root = ExponentialFunction(0, 0, 0)
square_root.set_mult_num('1')
square_root.set_base_num('2')
square_root.set_exp_num('1/2')

# Unit tests

# Cube root of 3 retrieved from https://www.calculator.net/
def test_cube_answer():
    assert(abs(cube_root.calculate_answer() - 1.4422495703) < 0.0000000001)

# Square root of 2 retrieved from https://www.calculator.net/
def test_square_answer():
    assert(abs(square_root.calculate_answer() - 1.4142135624) < 0.0000000001)

print("Test for Cube Root of 3")
print(cube_root.calculate_answer())
print("Test for Square Root of 2")
print(square_root.calculate_answer())
