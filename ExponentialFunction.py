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
    
    # represent_int is used to determine if passed string is integer or not   
    def represent_int(s):
        # Try to convert s to int, if it succeeds, return true
        try: 
            int(s)
            return True
        # If it fails, then catch the excpetion
        except ValueError:
            # Then convert to s to float and convert to int to check if equal
            n = float(s)
            m = int(n)
            # If n == m, then that means s is an integer
            if (m == n) :
                return True
            # Else, return False
            return False
            
    # special_root function is used to find root value when not a perfect root
    # root is the specific root to find, square, cube, etc.
    # num is the value to be rooted
    # i and j represent the range of values that will be searched for root
    def special_root(root, num, i, j):
        # Start at middle of range
        mid = (i + j)/2
        n = mid
        # Check if that is the answer
        for index in range(root - 1):
            n *= mid
        
        # If n is equal to num, or within an accepted uncertainty, 
        # then the function returns n
        if ((n == num) or (abs(num - n) < 0.000000001)):
            return mid
            
        # Else if n > num, then call root again, but between i and mid
        elif (n > num):
            return ExponentialFunction.special_root(root, num, i, mid)
        
        # Else, return root between mid and j
        else:
            return ExponentialFunction.special_root(root, num, mid, j)
        
    # get_root function is used to find the specific root of the passed value
    # root is the specific root, whether it be square, cube, etc.
    # num is the passed value to be rooted
    def get_root(root, num):
        # Initial guess is set to 1
        i = 1
        
        # The function then enters a while loop and only exits when result is 
        # True
        result = False
        while (result == False):
            # Check if num is a perfect root
            # Set n = i, then multiply it by i as many times as needed for 
            # root desired
            n = i
            for index in range(root - 1):
                n *= i
            
            # If n == num, then return n
            if (n == num):
                return i
            
            # If n > num, then num is not a perfect root, and need to call 
            # recursive function special_root
            # Since n > num, the root value lies between i-1 and i
            elif (n > num):
                i = ExponentialFunction.special_root(root, num, i - 1, i)
                return i
            
            # Increment i by 1 each time
            i += 1

    # calculate_answer is used to calculate the final answer from the input 
    # values
    def calculate_answer(self):
        # answer is set to 1 initially
        self.answer = 1.0
        
        # Check if exp_num is a fraction and split between numerator and 
        # denominator
        if '/' in self.exp_num:
            num, den = self.exp_num.split('/')
            
            # Check if num is an integer as well using represent_int
            if (ExponentialFunction.represent_int(num)):
                # Then check if den is an integer as well using represent_int
                if (ExponentialFunction.represent_int(den)):
                    d = int(den)
                    
                    # If d is 0, then the function returns None
                    if(d == 0):
                        self.answer = 0
                        return None
                        
                    # If d is negative, then d is and num are multiplied by -1
                    if(d < 0):
                        d *= -1
                        tempNum = int(num) * -1
                        num = str(tempNum)
                        
                    # Since exponent is fraction, the denominator represents a 
                    # root function
                    # Since anything to the power of 1/# is a root function
                    # use get_root to determine the new base_num
                    base_num = ExponentialFunction.get_root(d, self.base_num)
                    # A new ExponentialFunction object, temp, is used, so the 
                    # calling ExponentialFunction can keep original data
                    temp = ExponentialFunction(self.mult_num, base_num, 
                                                num, self.answer)
                    self.answer = temp.calculate_answer()
                    return self.answer
                
                # If den is a decimal, then multiply it by increment i until it 
                # is an integer
                # tempDen will temporarily store the variable den
                else:
                    i = 2
                    tempDen = den
                    
                    # If float(den) is 0, then the function returns None
                    if(float(den) == 0):
                        self.answer = 0
                        return None
                    
                    d = 0.0
                    while (ExponentialFunction.represent_int(tempDen) == 
                            False):
                        d = float(den)
                        d *= i
                        i += 1
                        tempDen = str(d)
                    
                    # If d is negative, then d is and num are multiplied by -1
                    if(d < 0):
                        d *= -1
                        tempNum = int(num) * -1
                        num = str(tempNum)
                    
                    # Once den becomes an integer, use get_root to determine 
                    # the new of base_num 
                    base_num = ExponentialFunction.get_root(int(d), 
                                                            self.base_num)
                    # Then multiply numerator by i - 1 to keep the exponent 
                    # equal since we multiplied the denominator, we have to 
                    # multiply numerator as well
                    n = int(num) * (i - 1)
                    # Set new exp_num and create new ExponentialFunction 
                    # object to calculate
                    exp_num = str(n)
                    temp = ExponentialFunction(self.mult_num, base_num, 
                                                exp_num, self.answer)
                    self.answer = temp.calculate_answer()
                    return self.answer
            
            # If num is a decimal, then it will have to be updated as well
            # tempNum will temporarily store the variable num
            else:
                i = 2
                tempNum = num
                n = 0.0
                while (ExponentialFunction.represent_int(tempNum) == False):
                    n = float(num)
                    n *= i
                    i += 1
                    tempNum = str(n)
                
                # Once num is an integer, then check if den is an integer
                if (ExponentialFunction.represent_int(den)):
                    # den is multiplied by i since num was converted to an int
                    d = int(den) * (i - 1)
                    
                    # If d is 0, then the function returns None 
                    if(d == 0):
                        self.answer = 0
                        return None
                        
                    # If d is negative, then d is and n are multiplied by -1
                    if(d < 0):
                        d *= -1
                        n *= -1
                        tempNum = str(n)
                        
                    # Use get_root to determine the new base_num
                    base_num = ExponentialFunction.get_root(d, self.base_num)
                    # Then create new ExponentialFunction to call 
                    # calculate_answer
                    temp = ExponentialFunction(self.mult_num, base_num, 
                                                tempNum, self.answer)
                    self.answer = temp.calculate_answer()
                    return self.answer
                
                # If den is a decimal, it will need to be converted as well
                # since num was converted to an integer, den is multiplied by 
                # the value of i - 1
                else:
                    j = 2
                    d = float(den) * (i - 1)
                    
                    # If d is 0, then the function returns None
                    if(d == 0):
                        self.answer = 0
                        return None
                        
                    den = str(d)
                    tempDen = den
                    while (ExponentialFunction.represent_int(tempDen) == 
                            False):
                        d = float(den)
                        d *= j
                        j += 1
                        tempDen = str(d)
                        
                    # If d is negative, then d is and num are multiplied by -1
                    if(d < 0):
                        d *= -1
                        n *= -1
                        
                    # Once den becomes an integer, use get_root to determine 
                    # the new base_num 
                    base_num = ExponentialFunction.get_root(int(d), 
                                                            self.base_num)
                    # Then updated exp_num by n and j before creating new 
                    # ExponentialFunction to call calculate_answer
                    n *= (j - 1)
                    tempExp = str(n)
                    temp = ExponentialFunction(self.mult_num, base_num, 
                                                tempExp, self.answer)
                    self.answer = temp.calculate_answer()
                    return self.answer
        
        # Then check that exp_num is an integer using represent_int
        elif (ExponentialFunction.represent_int(self.exp_num)):
            temp = float(self.exp_num)
            exp = int(temp)
            # If exp_num >= 0, then the answer is multiplied by the base_num, 
            # exp_num times
            if exp >= 0:
                for index in range(exp):
                    self.answer *= self.base_num
                # The final answer is retrieved after multiplying the current 
                # answer by mult_num
                self.answer *= self.mult_num
                return self.answer
        
            # If exp_num < 0, then the answer is multiplied by the base num, 
            # (-1 * exp_num) times
            elif exp < 0:
                for index in range(-1 * exp):
                    self.answer *= self.base_num
                # The final answer is retrieved after multiplying 
                # (1/current answer) by mult_num
                self.answer = self.mult_num * (1/self.answer)
                return self.answer
                
        # Finally, if the exponent is a decimal
        # The exponent will then be multiplied by increment i until it becomes 
        # an integer
        else:
            i = 2
            tempExp = self.exp_num
            e = 0.0
            while (ExponentialFunction.represent_int(tempExp) == False):
                e = float(self.exp_num)
                e *= i
                i += 1
                tempExp = str(e)
            # Once exp_num is an integer, use get_root to get new base after 
            # multiplying exponent
            base_num = ExponentialFunction.get_root((i - 1), self.base_num)
            # Then create new ExponentialFunction with new base_num and tempExp
            # as the exp_num before calling calculate_answer
            temp = ExponentialFunction(self.mult_num, base_num, tempExp, 
                                                self.answer)
            self.answer = temp.calculate_answer()
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
