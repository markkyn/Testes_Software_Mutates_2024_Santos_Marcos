import exceptions


# LogFunction class is used to calculate the logarithm expression logb(x)
class LogFunction:
    # Initialize 3 parameters for LogFunction
    # @param base: the base number
    # @param argument: the number whose logarithm is to be approximated
    # result is represent the final calculated result
    def __init__(self, base, argument):

        self.base = base
        self.argument = argument
        self.result = 0

    # set base number
    def set_base(self, base_num):
        # split and evaluate the string if input is fraction number
        if '/' in base_num:
            try:
                num, den = base_num.split('/')
                self.base = float(num) / float(den)
            except ZeroDivisionError:
                return None

        # set base to float of base_num if input is a number
        else:
            self.base = float(base_num)

        return self.base

    def set_argument(self, arg_num):
        # split and evaluate the string if input is fraction number
        if '/' in arg_num:
            try:
                num, den = arg_num.split('/')
                self.argument = float(num) / float(den)
            except ZeroDivisionError:
                return None

        # set argument to float of arg_num if input is a number
        else:
            self.argument = float(arg_num)

        return self.argument

    # get the value of base number and argument
    def set_values(self):
        # check the validation of base number
        while True:
            try:
                b_num = input("Please enter the value for b: ")
                if self.set_base(b_num) == 1:
                    raise exceptions.BaseNumError1
                elif self.base <= 0:
                    raise exceptions.BaseNumError2
                break
            except exceptions.BaseNumError1:
                print("Logarithm with base of 1 is undefined. Please enter a valid number")
            except exceptions.BaseNumError2:
                print("Logarithm with non-positive base is undefined. Please enter a valid number")
        self.set_base(b_num)
        # check the domain of argument
        while True:
            try:
                arg_num = input("Please enter the value for x: ")
                if self.set_argument(arg_num) <= 0:
                    raise exceptions.ArgumentError
                break
            except exceptions.ArgumentError:
                print("Error: Illegal argument. Value not in domain. Please enter a valid number")
        self.set_argument(arg_num)
        print("The function you entered is log(%s)(%s)" % (b_num, arg_num))

    # Implementation of the natural logarithm function using the Taylor series expansion
    # summation of ((-1) ** (i + 1)) * ((x - 1) ** i) / i
    # for i = 1 to n
    def ln_helper(self, x):

        if x >= 1:
            return self.ln_helper(x / 2) - self.ln_helper(0.5)  # ln(x) = ln(x*2 / 2) = ln(x*2) - ln(2)
        elif x < 0.5:
            return self.ln_helper(2 * x) + self.ln_helper(0.5)  # ln(x) = ln(x/2 * 2) = ln(x/2) + ln(2)
        n = 10000
        s = 0
        for i in range(1, n):
            s += ((-1) ** (i + 1)) * ((x - 1) ** i) / i
        return s

    # calculate the final result of log function by using logb(x) = ln(x) / ln(b)
    def cal_log(self):

        if self.argument > 0 and self.base > 0 and self.base != 1:
            self.result = self.ln_helper(self.argument) / self.ln_helper(self.base)
        return self.result

    # get the final result of log function
    def get_result(self):

        return self.result




