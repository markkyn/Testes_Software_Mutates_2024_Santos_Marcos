
import sys
sys.path.insert(0, './src')
from log import LogFunction
import math

"""
This module contains tests for log
module. It includes two set of
unit tests to approve the reasonable accuracy
of the answer for algebraic number
"""

function1 = LogFunction(0, 0)
function1.set_base("1/2")
function1.set_argument("100")
answer1 = function1.cal_log()

function2 = LogFunction(0, 0)
function2.set_base("1/3")
function2.set_argument("1/2")
answer2 = function2.cal_log()

function3 = LogFunction(0, 0)
function3.set_base("10")
function3.set_argument("-100")
answer3 = function3.cal_log()


# Unit test
def test_log_answer1():
    assert(answer1 - math.log(function1.argument, function1.base) < 0.0000000001)


def test_log_answer2():
    assert(answer2 - math.log(function2.argument, function2.base) < 0.0000000001)


print("The answer for log(1/2)(100) is %.10f" % answer1)
print("The answer for log(1/3)(1/2) is %.10f" % answer2)
print("The answer for log(10)(-100) is %.10f" % answer3)

