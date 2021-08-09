import re

# Math libarary will only be used for standard functions (sine, cos, tan, ...)
# No special functions will be calculated using this module
import math

# Special functions
from power_function import PowerFunction
from logarithm import LogFunction
from exponential_function import ExponentialFunction
from standard_deviation import StandardDeviation
from mad import MeanAbsoluteDeviation
from hyperbolic_sine import hyperbolic_sine

# Function regex
sine_regex = re.compile(r'(?:sin\(\-*\d*\.*\d*\))')
hyp_sine_regex = re.compile(r'(?:sinh\(\-*\d*\.*\d*\))')
cos_regex = re.compile(r'(?:cos\(\-*\d*\.*\d*\))')
parentheses_regex = re.compile(r'(?<=\()(?:\-*\d*\.*\d*(?:\+|\-|\/|\*)\-*\d*\.*\d*)+(?=\))')
pop_standard_dev_regex = re.compile(r'(?:pSD\[(?:\-*\d*\.*\d*\,*)*\])')
sample_standard_dev_regex = re.compile(r'(?:sSD\[(?:\-*\d*\.*\d*\,*)*\])')
mean_abs_dev_regex = re.compile(r'(?:mad\[(?:\-*\d*\.*\d*\,*)*\])')
power_regex = re.compile(r'(?:pow\(\-*\d+\.*\d*,\s*-*\d+\.*\d*\))')
exp_regex = re.compile(r'(?:exp\(\-*\d+\.*\d*,\s*-*\d+\.*\d*,\s*-*\d+\.*\d*\))')
logarithm_regex = re.compile(r'(?:log\(\-*\d+,\s*-*\d+\.*\d*\))')

# Extractor regex
param_regex = re.compile(r'(?<=\()(?:\s*\-*\d+\.*\d*\,*)*(?=\))')
list_regex = re.compile(r'(?<=\[)(?:\s*\-*\d+\.*\d*\,*)*(?=\])')


def parseEqu(s):

    # local, manipulatable, string
    _local_string = str(s)

    # Special functions objects
    __sinh = hyperbolic_sine(-1)
    __pow = PowerFunction("-1", "-1")
    __exp = ExponentialFunction(-1, -1, -1, -1)
    __log = LogFunction(-1, -1)
    __sd = StandardDeviation([])
    __mad = MeanAbsoluteDeviation([])

    print("Input String: " + _local_string)

    # Compute functions with values
    while True:
       
        if sine_regex.findall(_local_string):
            matc = sine_regex.findall(_local_string)
            for matches in matc:
                values = param_regex.findall(matches) # expecting 1 value
                ev = str(round(math.sin(float(values[0])), 10))
                _local_string = _local_string.replace(matches, ev)
            print("SIN changed string to -- " + _local_string)


        elif cos_regex.findall(_local_string):
            matc = cos_regex.findall(_local_string)
            for matches in matc:
                values = param_regex.findall(matches) # expecting 1 value
                ev = str(round(math.cos(float(values[0])), 10))
                _local_string = _local_string.replace(matches, ev)
            print("COS changed string to -- " + _local_string)

        elif hyp_sine_regex.findall(_local_string):
            matc = hyp_sine_regex.findall(_local_string)
            for matches in matc:
                values = param_regex.findall(matches) # expecting 1 value
                __sinh.set_value(float(values[0]))
                ev = str(round(__sinh.calculate_sinh(), 10))
                _local_string = _local_string.replace(matches, ev)
            print("SINH changed string to -- " + _local_string)

        elif power_regex.findall(_local_string):
            matc = power_regex.findall(_local_string)
            for matches in matc:
                values = param_regex.findall(matches)[0].split(',') # expecting 2 values
                __pow.set_base(values[0])
                __pow.set_exponent(values[1])
                ev = str(round(__pow.exponentFunction(), 10))
                _local_string = _local_string.replace(matches, ev)
            print("POW changed string to -- " + _local_string)

        elif exp_regex.findall(_local_string):
            matc = exp_regex.findall(_local_string)
            for matches in matc:
                values = param_regex.findall(matches)[0].split(',') # expecting 3 values
                __exp.set_mult_num(values[0])
                __exp.set_base_num(values[1])
                __exp.set_exp_num(values[2])
                __exp.calculate_answer()
                ev = str(round(__exp.answer, 10))
                _local_string = _local_string.replace(matches, ev)
            print("EXP changed string to -- " + _local_string)


        elif logarithm_regex.findall(_local_string):
            matc = logarithm_regex.findall(_local_string)
            for matches in matc:
                values = param_regex.findall(matches)[0].split(',') # expecting 2 values
                __log.set_base(values[0])
                __log.set_argument(values[1])
                ev = str(round(__log.cal_log(), 10))
                _local_string = _local_string.replace(matches, ev)
            print("LOG changed string to -- " + _local_string)

        elif pop_standard_dev_regex.findall(_local_string):
            matc = pop_standard_dev_regex.findall(_local_string)
            for matches in matc:
                values = list_regex.findall(matches)[0].strip('][').split(',') # expecting x values
                values = [float(x) for x in values]
                __sd.set_values(values) # Convert string values to float
                ev = str(round(__sd._population_standard_deviation(), 10))
                _local_string = _local_string.replace(matches, ev)
            print("pSD changed string to -- " + _local_string)

        elif sample_standard_dev_regex.findall(_local_string):
            matc = sample_standard_dev_regex.findall(_local_string)
            for matches in matc:
                values = list_regex.findall(matches)[0].strip('][').split(',') # expecting x values
                values = [float(x) for x in values]
                __sd.set_values(values) # Convert string values to float
                ev = str(round(__sd._sample_standard_deviation(), 10))
                _local_string = _local_string.replace(matches, ev)
            print("sSD changed string to -- " + _local_string)

        elif mean_abs_dev_regex.findall(_local_string):
            matc = mean_abs_dev_regex.findall(_local_string)
            for matches in matc:
                values = list_regex.findall(matches)[0].strip('][').split(',') # expecting x values
                values = [float(x) for x in values]
                __mad.set_values(values) # Convert string values to float
                ev = str(round(__mad.calculate_mad(), 10))
                _local_string = _local_string.replace(matches, ev)
            print("MAD changed string to -- " + _local_string)

        elif parentheses_regex.findall(_local_string):
            matc = parentheses_regex.findall(_local_string)
            for matches in matc:
                ev = str(round(eval(matches), 10))
                _local_string = _local_string.replace(matches, ev)
            #print("Literal Handling match: " + str(matc))
            print("Literal changed string to -- " + _local_string)

        else:
            break
    return str(eval(_local_string))


# Test cases
#string = '(((sin(22)+cos(332))*2+cos(cos(932)))/5)/sin(666)' #works
string = '(mad[sin(cos(212)+8*sinh(20)),232,2,1,554,665,3]/(pow(5,3)-exp(3,2,2)*log(16,77654)))+sSD[43,pow(8,2),cos(100),log(5,449)]'
print('Final Answer: ' + parseEqu(string))

# Use python's internal parser to parse the simple things (+, -, /, *, ())


