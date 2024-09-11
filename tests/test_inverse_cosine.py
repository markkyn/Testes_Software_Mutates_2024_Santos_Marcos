import math
import sys
sys.path.insert(0, './src')
from inverse_cosine import InverseCosine

pi = 3.141592653589793238462643383279502884197

function = InverseCosine(0)
function.set_values('-1')

x_over = InverseCosine(0)
x_over.set_values('3')

def test_indeterminacao():
    try:
        assert(x_over.calculate_acos() == None)
    except ValueError:
        print("Indeterminação de valores")


def test_answer():
    assert (abs(function.calculate_acos() - math.acos(function.get_values())) < 0.0001)


print(test_answer())
print()