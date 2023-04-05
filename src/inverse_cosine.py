import math

"""
This module implements the Inverse cosine function for the calculator.
"""


class InverseCosine:
    # This class uses taylor series to calculate arcsin and then applies trigonometric identities for various
    # domains for arccos
    # value - attribute representing the input value for the function

    pi = 3.141592653589793238462643383279502884197

    def __init__(self, value):
        # constructer of the class
        self.value = value

    # mutator method for values
    def set_values(self, value):
        # If the value is a fraction, then split into numerator and denominator
        # Then set value to numerator/denominator
        # If there is a division by zero, the exception is caught and thrown &
        # function returns None
        if '/' in value:
            try:
                num, den = value.split('/')
                self.value = float(num) / float(den)
            except ZeroDivisionError:
                print("ZeroDivisionError -- ")
                # to be added - raise
                return None
        # Else, set self.value to float of value
        else:
            self.value = float(value)

        return self.value

    # Accessor for values.
    def get_values(self):
        return self.value

    # Helper function that calculates the square root.
    def __sqrt(n):
        ans = n ** 0.5
        return ans

    # Helper function to calculate arcsin using the taylor series.
    def __asin_taylor_sum(self, value):
        temp = value
        factor = 1.0
        divisor = 1.0
        asin_sum = value

        for i in range(0, 40):
            temp *= value * value
            divisor *= 2.0
            factor *= (2.0 * i + 1.0) / ((i + 1.0) * 2.0)
            asin_sum += (factor * temp) / divisor
        return asin_sum

    # Helper function to implement a shader implementation for arcsin based on intervals.
    # Minor issues with sqrt function.. hence used math.sqrt for now
    # abs value will be changed to multiplication to -1 if neg( to be implemented)
    def __asin(self, value):
        if abs(value) <= 0.71:
            return self.__asin_taylor_sum(value)
        elif value > 0:
            temp = float(1.0 - (value * value))
            return (self.pi / 2.0) - self.__asin_taylor_sum(math.sqrt(temp))
        else:
            temp = float(1.0 - (value * value))
            return self.__asin_taylor_sum(math.sqrt(temp)) - (self.pi / 2.0)

    # Function to calculate arccos using trignometric identities involving arcsin.
    def calculate_acos(self):
        return (self.pi / 2.0) - self.__asin(self.value)
