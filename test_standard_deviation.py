import decimal
import sys
from standard_deviation import StandardDeviation

# Create a StandardDeviation object
std = StandardDeviation(75, 89, 94, 13, 42, 77, 40)

def test_mean():
    assert(std.get_mean() == 61.42857142857)

def test_population_standard_deviation():
    assert(std.get_psd() == 27.85091505476)

def test_sample_standard_deviation():
    assert(std.get_ssd() == 30.08242644722)