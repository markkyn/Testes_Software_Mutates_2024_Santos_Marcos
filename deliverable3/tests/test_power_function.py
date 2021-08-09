import sys
sys.path.insert(0, './deliverable3/src')
from power_function import PowerFunction


test = PowerFunction(10, 2)

def test_exponential_function():
    assert(abs(test.exponentFunction() - 100) < 0.0000000001)

print(test_exponential_function())