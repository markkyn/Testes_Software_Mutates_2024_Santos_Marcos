from ExponentialFunction import ExponentialFunction

# Start with simple ExponentialFunction option where all values are 0
function = ExponentialFunction(0,0,0,0)

# Display format of Exponential Function
print('ab' + ExponentialFunction.get_super('x'))

# Ask the user to input the value for a
mNum = input("Enter value for a: ")

# If the user enters a fraction, then split into numerator and denominator
# And pass the value of num/den in set_mult_num
if '/' in mNum:
    num, den = mNum.split('/')
    function.set_mult_num(float(num)/float(den))

# Else, pass mNum as float
else :
    function.set_mult_num(float(mNum))

# Then ask the user to enter the value for b, and perform the same checks
bNum = input("Enter value for b: ")

if '/' in bNum:
    num, den = bNum.split('/')
    function.set_base_num(float(num)/float(den))
    
else :
    function.set_base_num(float(bNum))

# Ask the user to enter the value for x
eNum = input("Enter value for x: ")
function.set_exp_num(eNum)

print(function.calculate_answer())
print(function)
