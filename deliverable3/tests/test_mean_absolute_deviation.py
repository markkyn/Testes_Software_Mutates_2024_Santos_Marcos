"""
This module contains tests for mean absolute
deviation module and its functions.
The MeanAbsoluteDeviation object is initialied
with a random set of numbers and expressions to
reflect real application. Each function of the
object is tested against an accurately calcualted
value to ensure the margin of error remains within
2%.
"""

import sys
sys.path.insert(0, './deliverable3/src')
from mean_absolute_deviation import MeanAbsoluteDeviation
import math

# Prior to running unit tests using pytest
# the input test must be commented out
print('Set of values: sin(332), sinh(2.2212), 8**2, 6**(((212/100)**2)/88), (43/2)**2, ((cos(99) - sin(33))/5), 32')
mean_abs_dev = MeanAbsoluteDeviation([math.sin(332), math.sinh(2.2212), 8**2, 6**(((212/100)**2)/88), (43/2)**2, ((math.cos(99) - math.sin(33))/5), 32])




# Unit tests
# math.sin(332)                         --> -0.46947
# math.sinh(2.2212)                     --> 4.55495
# 8**2                                  -->   64
# 6**(((212/100)**2)/88)                --> 1.04067
# (43/2)**2                             --> 462.25
# ((math.cos(99) - math.sin(33))/5)     --> -0.14021
# 32                                    -->  32


# Asserted against mean from
# https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php
def test_mean():
    assert(abs(mean_abs_dev.get_mean() - 80.462277142857) < 0.02)  #Error less than 2% is acceptable

# Asserted against mean absolute deviation from
# https://ncalculators.com/statistics/mean-absolute-deviation-calculator.htm
def test_mean():
    assert(abs(mean_abs_dev.get_mad() - 109.0822) < 0.02)   #Error less than 2% is acceptable



print(mean_abs_dev.get_mean())
print(mean_abs_dev.get_mad())


# # Input test case
# if input('Would you like to test the module with your own input?(y/n)') == 'y':
#     numbers = input('Please provide numbers separated by comma to calculate the standard deviation \n'
#                     'Example: 7,9,20,20,13,20,18,13')
#     numbers = numbers.split(',')

#     std = StandardDeviation()
#     for i in numbers:
#         std.add_values(int(i))

#     print(std.get_mean())
#     print(std.get_psd())
#     print(std.get_ssd())