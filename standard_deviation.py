class StandardDeviation:
    _n_values = 0
    def __init__(self, *values):
        self._values = values
        for v in values:
            self._n_values += 1
        self._psd = self.population_standard_deviation()
        self._ssd = self.sample_standard_deviation()


    def add_values(self, *values):
        self._values = self._values + values
        for v in values:
            self._n_values += 1
        self._psd = self.population_standard_deviation()
        self._ssd = self.sample_standard_deviation()

    def mean(self):
        total = 0
        for v in self._values:
            total += v
        
        return total/self._n_values
 
    def population_standard_deviation(self):
        total = 0
        mean = self.mean()
        for v in self._values:
            total += (v - mean) ** 2

        return (total/ self._n_values) ** 0.5

    
    def sample_standard_deviation(self):
        total = 0
        mean = self.mean()
        for v in self._values:
            total += (v - mean) ** 2
        
        return (total / (self._n_values - 1)) ** 0.5
