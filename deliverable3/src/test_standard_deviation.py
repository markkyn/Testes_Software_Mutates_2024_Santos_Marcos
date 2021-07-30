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

std = StandardDeviation(75/7, 89/3, 94/5, 13/4, 42/5, 77/3, 40/6)

# Unit tests
def test_mean():
    assert(abs(std.get_mean() - 14.737755102053) < 0.0000000001)

def test_population_standard_deviation():
    assert(abs(std.get_psd() - 9.352476933703) < 0.0000000001)

def test_sample_standard_deviation():
    assert((std.get_ssd() - 10.101829649195) < 0.0000000001)

# Input test case
numbers = input('Please provide numbers separated by comma to calculate the standard deviation \nExample: 7,9,20,20,13,20,18,13')
numbers = numbers.split(',')

std = StandardDeviation()
for i in numbers:
    std.add_values(int(i))

print(std.get_mean())
print(std.get_psd())
print(std.get_ssd())