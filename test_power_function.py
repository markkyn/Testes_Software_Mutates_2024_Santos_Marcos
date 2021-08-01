import function

base = input("Enter your base: ")
exponent = input("Enter your exponent: ")
test = function.PowerFunction(base, exponent)
print(test.exponentFunction())

def test_exponential_function():
    assert(abs(test - 100) < 0.0000000001)

test_exponential_function()