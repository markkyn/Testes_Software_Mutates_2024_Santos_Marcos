"""
This module is a unit test for standard_deviation
module and its functions.
A StandardDeviation object is created using
random numbers and used to check the precision
of the __mean, _population_standard_deviation, 
and _sample_standard_deviation functions.
"""

import sys
from standard_deviation import StandardDeviation
import math

print('Set of values: 2**(1/2), ((3**(1/3))/2, 4**7, 13/4, sin(333), cos(963), 17')
std = StandardDeviation(2**(1./2), (3**(1./3))/2, 4**7, 13/4, math.sin(333), math.cos(963), 17)

# Unit tests
def test_mean():
    assert(abs(std.get_mean() - 2343.7535487876) < 0.0000000001)

def test_population_standard_deviation():
    assert(abs(std.get_psd() - 5731.9093454445) < 0.0000000001)

def test_sample_standard_deviation():
    assert((std.get_ssd() - 6191.1696957677) < 0.0000000001)

print(std.get_mean())
print(std.get_psd())
print(std.get_ssd())

# Input test case
numbers = input('Please provide numbers separated by comma to calculate the standard deviation \nExample: 7,9,20,20,13,20,18,13')
numbers = numbers.split(',')

std = StandardDeviation()
for i in numbers:
    std.add_values(int(i))

print(std.get_mean())
print(std.get_psd())
print(std.get_ssd())