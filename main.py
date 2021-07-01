from ExponentialFunction import ExponentialFunction

function = ExponentialFunction(0,0,0,0)
print('ab' + ExponentialFunction.get_super('x'))
mNum = input("Enter value for a: ")
function.set_Mult_Num(float(mNum))
bNum = input("Enter value for b: ")
function.set_Base_Num(float(bNum))
eNum = input("Enter value for x: ")
function.set_Exp_Num(float(eNum))
print(function.calculateAnswer())
print(function)
