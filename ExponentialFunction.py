# ExponentialFunction class is used for evaluating Exponential Function ab^x
# The instance of the class is then stored in calculator history
class ExponentialFunction:

    # ExponentialFunction has 4 parameters
    # mult_num = a in the function, which is what gets multiplied to b^x
    # base_num = b in the function, which is the base of the function
    # exp_num = x in the function, which is the power the base is multiplied by
    # answer, which is the answer after calculating
    def __init__(self, mult_num, base_num, exp_num, answer):
        self.mult_num = mult_num
        self.base_num = base_num
        self.exp_num = exp_num
        self.answer = answer

    # set_Mult_Num sets the value of mult_num
    def set_mult_num(self, mNum):
        # If the mNum is a fraction, then split into numerator and denominator
        # Then set mult_num to numerator/denominator
        if '/' in mNum:
            num, den = mNum.split('/')
            self.mult_num = float(num)/float(den)

        # Else, set mult_num to float of mNum
        else:
            self.mult_num = float(mNum)
  
    #set_Base_Num sets the value of base_num
    def set_base_num(self, bNum):
        # If bNum is a fraction, then split into numerator and denominator
        if '/' in bNum:
            num, den = bNum.split('/')
            self.base_num = float(num)/float(den)
        # Else, set base_num to float of bNum
        else:
            self.base_num = float(bNum)

    # set_Exp_Num sets the value of exp_num
    def set_exp_num(self, eNum):
        self.exp_num = eNum
        
    def set_values(self):
        # Display format of Exponential Function
        print('ab' + ExponentialFunction.get_super('x'))

        # Ask the user to input the value for a
        mNum = input("Enter value for a: ")
        self.set_mult_num(mNum)

        # Then ask the user to enter the value for b, and perform the same 
        # checks
        bNum = input("Enter value for b: ")
        self.set_base_num(bNum)

        # Ask the user to enter the value for x
        eNum = input("Enter value for x: ")
        self.set_exp_num(eNum)

    # calculate_answer is used to calculate the final answer from the input 
    # values
    # Since Python has a exponential arithmetic operator, that will be used
    def calculate_answer(self):
        # First have to convert exp_num to a value since it is still a string
        # If exp_num is a fraction, then break it into numerator and 
        # denomintaor and calculate answer
        if '/' in self.exp_num:
            num, den = self.exp_num.split('/')
            # Division by zero is handled by trying to divide numerator and
            # denominator and catching a ZeroDivisionError error
            try:
                exp = float(num)/float(den)
                self.answer = (self.mult_num)*(self.base_num**exp)
                return self.answer
            # If the denominator is 0, the function returns None
            except ZeroDivisionError:
                return None
        # Else, the exp_num is assumed to be an integer or float and is 
        # converted
        else:
            exp = float(self.exp_num)
            self.answer = (self.mult_num)*(self.base_num**exp)
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
