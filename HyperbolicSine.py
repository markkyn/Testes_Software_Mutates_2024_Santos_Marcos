import math

''' hyperbolic_sine class is used to calculate Sinh(x).
Which x can be a real or complex number.
The instance of the class is then stored in calculator history. '''


class HyperbolicSine:
    '''
    Function: hyperbolic_sine constructor
    Inputs:
        Value - Is the real number or complex number which we want to calculate Sinh on
    Outputs:
        Instance of this Class. It has the euler number defined in it's own and a value as the input.    
    '''

    def __init__(self, value):
        self._value = value
        self._euler_num = math.e
        self._sinh = 0

    # In this function we calculate e^x and return the value
    def _calculate_exponential(self, value):
        return math.e ** value

    # In this function, we calculate the numerator of Sinh which is e^x - e^-x
    def _calculate_numerator(self, value):
        return (self._calculate_exponential(value) -
                self._calculate_exponential(-1 * value))

    # In this function, we calculate Sinh which is (e^x - e^-x)/2
    def calculate_sinh(self):
        self._sinh = (self._calculate_numerator(self._value)) / 2
        return self._sinh

    # Returns the instanced value list
    def get_value(self):
        return self._value

    # Set instanced value
    def set_value(self, new_value):
        self._value = new_value

    # Returns the Sinh value
    def get_sinh(self):
        return self._sinh


# Sample for Checking the value of Sinh(3)
#x = HyperbolicSine(3)
#print(x.calculate_sinh())

