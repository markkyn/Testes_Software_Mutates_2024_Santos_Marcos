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
  def set_Mult_Num(self, mNum):
    self.mult_num = mNum
  
  #set_Base_Num sets the value of base_num
  def set_Base_Num(self, bNum):
    self.base_num = bNum

  # set_Exp_Num sets the value of exp_num
  def set_Exp_Num(self, eNum):
    self.exp_num = eNum

  # calculateAnswer is used to calculate the final answer from the input values
  def calculateAnswer(self):
    # answer is set to 1 initially
    self.answer = 1
    # if exp_num >= 0, then the answer is multiplied by the base_num, exp_num times
    if self.exp_num >= 0:
      for index in range(self.exp_num):
        self.answer = self.answer * self.base_num
      # The final answer is retrieved after multiplying the current answer by mult_num
      self.answer = self.answer * self.mult_num
      return self.answer
    # if exp_num < 0, then the answer is multiplied by the base num, (-1 * exp_num) times
    elif self.exp_num < 0:
      for index in range(-1 * self.exp_num):
        self.answer = self.answer * self.base_num
      # The final answer is retrieved after multiplying (1/current answer) by mult_num
      self.answer = self.mult_num * (1/self.answer)
      return self.answer
  
  # get_super method is used to print exponents 
  # source: https://www.geeksforgeeks.org/how-to-print-superscript-and-subscript-in-python/
  # function converts passed string x to superscript
  def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

  # str function is used to display the exponential function using the sympy package
  def __str__(self):
    return str(self.mult_num) + '(' + str(self.base_num) + ExponentialFunction.get_super(str(self.exp_num)) + ')' + ' = ' + str(self.answer)
