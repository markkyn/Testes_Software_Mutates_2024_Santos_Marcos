import math
import log

function = log.LogFunction(0, 0)
function.set_values()
answer = function.cal_log()
print("For reasonable accuracy, we keep 10 decimals after the point.")
print("The answer is %.10f" % answer)
print("The built-in python log answer is %.10f" % math.log(function.argument, function.base))
