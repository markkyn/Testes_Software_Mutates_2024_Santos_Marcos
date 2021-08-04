from hyperbolic_sine import HyperbolicSine

#Checking Sinh(2.5)
sinh = HyperbolicSine(2.5)
x = sinh.calculate_sinh()

#Checking Sinh(3)
sinh.set_value(3)
y = sinh.calculate_sinh()

#Checking Sinh(2+2j)
sinh.set_value(2+2j)
z = sinh.calculate_sinh()

print(x)
print(y)
print(z)
print((x*y) + z)