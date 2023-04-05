# coding=utf-8
# ExponentialFunction class is used for evaluating Exponential Function ab^x
# The instance of the class is then stored in calculator history
class ExponentialFunction:

    # ExponentialFunction has 4 parameters
    # mult_num = a in the function, which is what gets multiplied to b^x
    # base_num = b in the function, which is the base of the function
    # exp_num = x in the function, which is the power the base is multiplied by
    # answer, which is the answer after calculating
    def __init__(self, mult_num, base_num, exp_num):
        self.mult_num = mult_num
        self.base_num = base_num
        self.exp_num = exp_num
        self.answer = 0

    # set_mult_num sets the value of mult_num
    def set_mult_num(self, m_num):
        # If the mNum is a fraction, then split into numerator and denominator
        # Then set mult_num to numerator/denominator
        # If there is a division by zero, the exception is caught and the
        # ZeroDivisionError is raised
        if '/' in m_num:
            try:
                num, den = m_num.split('/')
                if float(den) == 0:
                    raise ZeroDivisionError
                self.mult_num = float(num) / float(den)
                return self.mult_num
            except ZeroDivisionError:
                return None
        # Else, set mult_num to float of mNum
        else:
            self.mult_num = float(m_num)
            return self.mult_num
  
    #set_base_num sets the value of base_num
    def set_base_num(self, b_num):
        # If bNum is a fraction, then split into numerator and denominator
        # If there is a division by zero, the exception is caught and
        # The function returns None
        if '/' in b_num:
            try:
                num, den = b_num.split('/')
                if float(den) == 0:
                    raise ZeroDivisionError
                self.base_num = float(num) / float(den)
                return self.base_num
            except ZeroDivisionError:
                # Raise ZeroDivisionError
                raise ZeroDivisionError
                return None
        # Else, set base_num to float of b_num
        else:
            self.base_num = float(b_num)
            return self.base_num

    # set_exp_num sets the value of exp_num
    def set_exp_num(self, e_num):
        # If e_num is a fraction, then split into numerator and denominator
        # If there is a division by zero, the exception is caught and
        # The function returns None
        if '/' in e_num:
            try:
                num, den = e_num.split('/')
                if float(den) == 0:
                    raise ZeroDivisionError
                self.exp_num = float(num) / float(den)
                return self.exp_num
            except ZeroDivisionError:
                # Raise ZeroDivisionError
                raise ZeroDivisionError
                return None
        # Else, set exp_num to float of bNum
        else:
            self.exp_num = float(e_num)
            return self.exp_num
            
    # get_mult_num returns the value of mult_num
    def get_mult_num(self):
        return self.mult_num
        
    # get_base_num returns the value of base_num
    def get_base_num(self):
        return self.base_num
        
    # get_exp_num returns the value of exp_num
    def get_exp_num(self):
        return self.exp_num

    # calculate_answer is used to calculate the final answer from the input 
    # values
    # Since Python has an exponential arithmetic operator, that will be used
    def calculate_answer(self):
        # The answer is obtained using the values obtained from the set 
        # functions above
        # Any Division By Zero was handled in the set functions
        self.answer = (self.mult_num) * (self.base_num ** self.exp_num)
        return self.answer
        
    # get_super method is used to print exponents 
    # Fnction converts passed string x to superscript
    # GeeksforGeeks (2021) get_super source code (Version 1.0) [Source code].
    #   https://www.geeksforgeeks.org/how-to-print-superscript-and-subscript-in
    #   -python/
    def get_super(x):
        normal = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
                    "0123456789+-=()")
        super_s = ("ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ" 
                    "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾")
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)
        
    # str function is used to display the exponential function 
    def __str__(self):
        return (str(self.mult_num) + '(' + str(self.base_num) 
                + ExponentialFunction.get_super(str(self.exp_num)) + ')' 
                + ' = ' + str(self.answer))
