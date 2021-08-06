import sys
sys.path.insert(0, './deliverable3/src')
from hyperbolic_sine import HyperbolicSine
import math



# Using python's calculator to test if our calculator has enough accuracy or not.
Sinh = HyperbolicSine(3)


def test_answer():
    assert(abs(Sinh.calculate_sinh() - math.sinh(Sinh.get_value())) < 0.0000000001)


print(test_answer())
# The accuracy was exactly what we wanted.
