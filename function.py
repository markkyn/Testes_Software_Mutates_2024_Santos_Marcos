class PowerFunction: 
    # Receives the string "base"
    # Sets the base of the function 
    def set_base(self, base): 
        # Check if the base is a real number
        # If yes, separate both nums/denum of the fraction and return value
        if("/" in base):
            try:
                numerator = base[0:base.index('/')]
                denumerator = base[base.index('/') + 1:]
                self.base = float(numerator)/float(denumerator)
            except ZeroDivisionError: 
                print("Can't do division by zero!")
        else:
            self.base = float(base)

    # Receives the string "exponent"
    # Sets the base of the function 
    def set_exponent(self, exponent):
        # Check if the exponent is a real number
        # If yes, separate both nums/denum of the fraction and return value
        if("/" in exponent):
            try:
                numerator = exponent[0:exponent.index('/')]
                denumerator = exponent[exponent.index('/') + 1:]
                self.exponent = float(numerator)/float(denumerator)
            except ZeroDivisionError: 
                print("Can't do division by zero!")
        else:
            self.exponent = float(exponent)
    #PowerFunction parameters:
    # base : Represents the input base (x) of the function
    # exponent : Represents the input exponent (y) of the function 
    def __init__(self, base, exponent):
        self.set_base(base)
        self.set_exponent(exponent)

    # Does the operation
    def exponentFunction(self):
        return (self.base**self.exponent)

    # Printing the base and exponent
    def __str__(self):
        return ("Base: " + str(self.base) + " Exponent: " + str(self.exponent))


base = input("Enter your base: ")
exponent = input("Enter your exponent: ")
test = PowerFunction(base, exponent)
print(test.exponentFunction())