import sys
sys.path.insert(0, './deliverable3/src')
import power_function

##For base: enter 10
base = input("Enter your base: ")
##For exponent: enter 2
exponent = input("Enter your exponent: ")
test = power_function.PowerFunction(base, exponent)

def test_exponential_function():
    assert(abs(test.exponentFunction() - 100) < 0.0000000001)

print(test_exponential_function())