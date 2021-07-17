class StandardDeviation:
    _n_values = 0
    def __init__(self, *values):
        self._values = values
        for v in values:
            self._n_values += 1
        self._mean = self.__mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def get_values(self):
        return self._values

    def set_values(self, *values):
        self._values = values
        self._n_values = 0
        for v in values:
            self._n_values += 1
        self._mean = self.__mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def get_n_values(self):
        return self._n_values
    
    def get_mean(self):
        return self._mean
    
    def get_psd(self):
        return self._psd

    def get_ssd(self):
        return self._ssd

    def add_values(self, *values):
        self._values = self._values + values
        for v in values:
            self._n_values += 1
        self._mean = self.__mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def __mean(self):
        total = 0
        for v in self._values:
            total += v
        
        return total/self._n_values
 
    def _population_standard_deviation(self):
        total = 0
        mean = self.__mean()
        for v in self._values:
            total += (v - mean) ** 2

        return (total/ self._n_values) ** 0.5

    
    def _sample_standard_deviation(self):
        total = 0
        mean = self.__mean()
        for v in self._values:
            total += (v - mean) ** 2
        
        return (total / (self._n_values - 1)) ** 0.5

std = StandardDeviation(10, 12, 23, 23, 16, 23, 21, 16)
print("Enter values:", std.get_values())
print(std.get_n_values(), "values were entered.")
print("Mean: ", std.get_mean())
print("Population Standard Deviation: ", std.get_psd())
print("Sample Standard Deviation: ", std.get_ssd())
std.set_values(10, 12, 23, 23, 16, 23)
print("Enter values:", std.get_values())
print(std.get_n_values(), "values were entered.")
print("Mean: ", std.get_mean())
print("Population Standard Deviation: ", std.get_psd())
print("Sample Standard Deviation: ", std.get_ssd())
std.add_values(21, 16)
print("Enter values:", std.get_values())
print(std.get_n_values(), "values were entered.")
print("Mean: ", std.get_mean())
print("Population Standard Deviation: ", std.get_psd())
print("Sample Standard Deviation: ", std.get_ssd())