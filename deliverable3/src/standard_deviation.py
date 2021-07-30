"""
This module implements the standard deviation function for the calculator.
"""
class StandardDeviation:
    """
    This class encapsulates functionality for the standard deviation function as an object.
    _values - private attribute representing the values of the set.
    _n_values - private class variable representing the number of values of the set.
    _mean - private attribute representing the mean of the set.
    _psd - private attribute representing the population standard deviation of the set.
    _ssd - private attribute representing the sample standard deviation of the set.
    """

    _n_values = 0
    def __init__(self, *values):
        """
        Class constructor initializes _values with the given values,
        increments _n_values based on the number of values, and initializes
        the rest of the attributes using their respective functions.
        In case no values have been entered _values and _n_values are
        both set to None. 
        """
        if len(values) == 0:
            self._values = None
            self._n_values = None
        else:
            self._values = values
            for v in values:
                self._n_values += 1
        self._mean = self.__mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def get_values(self):
        """ Accessor for _values. """
        return self._values

    def set_values(self, *values):
        """
        Mutator for _values that updates other
        attributes based on the new set values.
        """
        self._values = values
        self._n_values = 0
        for v in values:
            self._n_values += 1
        self._mean = self.__mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def get_n_values(self):
        """ Accessor for _n_values. """
        return self._n_values
    
    def get_mean(self):
        """ Accessor for _mean. """
        return self._mean
    
    def get_psd(self):
        """ Accessor for _psd. """
        return self._psd

    def get_ssd(self):
        """ Accessor for _ssd. """
        return self._ssd

    def add_values(self, *values):
        """
        Utility function that adds values to the existing set of values
        and updates the other attributes based on the new set of values.
        """ 
        self._values = self._values + values
        for v in values:
            self._n_values += 1
        self._mean = self.__mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def __mean(self):
        """
        Private function that calculates the mean of the set.
        """
        total = 0
        for v in self._values:
            total += v
        
        return total/self._n_values
 
    def _population_standard_deviation(self):
        """
        Private function that calculates the population standard deviation.
        """
        total = 0
        mean = self.__mean()
        for v in self._values:
            total += (v - mean) ** 2

        return (total/ self._n_values) ** 0.5

    
    def _sample_standard_deviation(self):
        """
        Private function that calculates the sample standard deviation.
        """       
        total = 0
        mean = self.__mean()
        for v in self._values:
            total += (v - mean) ** 2
        
        return (total / (self._n_values - 1)) ** 0.5