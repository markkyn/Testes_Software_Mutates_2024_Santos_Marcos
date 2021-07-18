import sys
from standard_deviation import StandardDeviation

std = StandardDeviation(75, 89, 94, 13, 42, 77, 40)

def test_mean():
    assert(abs(std.get_mean() - 61.42857142857) < 0.0000000001)

def test_population_standard_deviation():
    assert(abs(std.get_psd() - 27.85091505476) < 0.0000000001)

def test_sample_standard_deviation():
    assert((std.get_ssd() - 30.08242644722) < 0.0000000001)