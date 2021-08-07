# This module contains the test for log function, user can input the base number and argument number.
# The first answer is from the log function class and the second one is from built-in math library
# in python. From the comparation of two result, we can see the accuracy is 100%.
import sys
sys.path.insert(0, './deliverable3/src')
from log import LogFunction
import math

function = log.LogFunction(0, 0)
function.set_values()
answer = function.cal_log()
print("For reasonable accuracy, we keep 10 decimals after the point.")
print("The answer is %.10f" % answer)
print("The built-in python log answer is %.10f" % math.log(function.argument, function.base))
