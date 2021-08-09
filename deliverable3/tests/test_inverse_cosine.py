import math
import sys
from inverse_cosine import InverseCosine

pi = 3.141592653589793238462643383279502884197

function = InverseCosine(0.4)
function.set_values('1/2')

## test1
## yet to fix max error, correct upto 2 decimal places
print("Test 1")
print(function.calculate_acos())
print(math.acos(0.5))

## test2
function1 = InverseCosine(0.2)
function2 = InverseCosine(0.9)
function3 = InverseCosine(-0.5)

print("Test 2")
print(math.acos(0.2) - math.acos(0.9) * math.acos(-0.5))
print(function1.calculate_acos() - function2.calculate_acos() * function3.calculate_acos())
