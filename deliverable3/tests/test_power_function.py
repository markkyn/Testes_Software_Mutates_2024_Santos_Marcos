import sys

from deliverable3.src.power_function import PowerFunction

sys.path.insert(0, '../deliverable3/src')

##For base: enter 10
# base = input("Enter your base: ")
# ##For exponent: enter 2
# exponent = input("Enter your exponent: ")
test = PowerFunction(10, 2)

def test_exponential_function():
    assert(abs(test.exponentFunction() - 100) < 0.0000000001)

print(test_exponential_function())