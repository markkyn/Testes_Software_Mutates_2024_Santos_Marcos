class StandardDeviation:
    n_values = 0
    def __init__(self, *values):
        self.values = values
        for v in values:
            self.n_values += 1

    def mean(self):
        total = 0
        for v in self.values:
            total += v
        
        return total/self.n_values
 
    def population_standard_deviation(self):
        total = 0
        mean = self.mean()
        for v in self.values:
            total += (v - mean) ** 2

        return (total/ self.n_values) ** 0.5

    
    def sample_standard_deviation(self):
        total = 0
        mean = self.mean()
        for v in self.values:
            total += (v - mean) ** 2
        
        return (total / (self.n_values - 1)) ** 0.5
