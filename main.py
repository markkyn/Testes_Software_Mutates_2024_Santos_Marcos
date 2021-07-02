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

# If the user enters an integer, then pass it as integer in set_mult_num
# Determine if it's an integer using isdigit method
elif mNum.isdigit():
    function.set_mult_num(int(mNum))

# Finally, if mNum is decimal, then pass it as float(mNum)
else :
    function.set_mult_num(float(mNum))

# Then ask the user to enter the value for b, and perform the same checks
bNum = input("Enter value for b: ")

if '/' in bNum:
    num, den = bNum.split('/')
    function.set_base_num(float(num)/float(den))
    
elif bNum.isdigit():
    function.set_base_num(int(bNum))
    
else :
    function.set_mult_num(float(bNum))

# Ask the user to enter the value for x
eNum = input("Enter value for x: ")
function.set_exp_num(int(eNum))

print(function.calculate_answer())
print(function)
