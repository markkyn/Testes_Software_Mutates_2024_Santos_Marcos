class StandardDeviation:
    _n_values = 0
    def __init__(self, *values):
        self._values = values
        for v in values:
            self._n_values += 1
        self._mean = self._mean()
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def get_values(self):
        return self._values

    def get_n_values(self):
        return self._n_values
    
    def get_psd(self):
        return self._psd

    def get_ssd(self):
        return self._ssd

    def add_values(self, *values):
        self._values = self._values + values
        for v in values:
            self._n_values += 1
        self._psd = self._population_standard_deviation()
        self._ssd = self._sample_standard_deviation()

    def _mean(self):
        total = 0
        for v in self._values:
            total += v
        
        return total/self._n_values
 
    def _population_standard_deviation(self):
        total = 0
        mean = self._mean()
        for v in self._values:
            total += (v - mean) ** 2

        return (total/ self._n_values) ** 0.5

    
    def _sample_standard_deviation(self):
        total = 0
        mean = self._mean()
        for v in self._values:
            total += (v - mean) ** 2
        
        return (total / (self._n_values - 1)) ** 0.5
