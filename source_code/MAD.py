# MeanAbsoluteDeviation class is used to calculate the mean absolute deviation
# of a list of values.
# The instance of the class is then stored in calculator history
class MeanAbsoluteDeviation:


    # MeanAbsoluteDeviation only has 1 parameter:
    # values = the list of values to perform the MAD function on
    def __init__(self, values):
        self._values = values
        self._mean = 0
        self._mad = 0


    # Private method
    # Calculates the mean (average) of the values
    def __calculate_mean(self, value_array):
        num_of_vals = len(value_array)

        # Calculate the sum
        total = 0
        for val in list(value_array):
            total += val
        # Calculate and return the mean
        return total / num_of_vals

    # Public method
    # Calculates (and returns) the mean absolute deviation
    def calculate_mad(self):
        num_of_vals = len(self._values)

        # Calculate the mean
        self._mean = self.__calculate_mean(self._values)

        # Calculate MAD
        total = 0
        diff = 0
        # Calculate the sum of the differences
        for val in list(self._values):
            diff = val - self._mean
            if diff < 0:
                diff *= (-1)
            total += diff
        self._mad = total / num_of_vals

        return self._mad



    # Returns the currently stored mean absolute deviation value.
    # It will be 0 in the case that calculate_mad() isnt called.
    def get_mad(self):
        return self._mad

    # Returns the currently stored mean value.
    # It will be 0 in the case that calculate_mad() isnt called.
    def get_mean(self):
        self._mean

    # Resets the instanced value list
    # Does not change the previously calculated MAD or mean
    def set_values(self, new_values):
        self._values = new_values

    # Returns the instanced value list
    def get_values(self):
        return self._values