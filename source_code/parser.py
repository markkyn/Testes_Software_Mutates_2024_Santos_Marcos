import re

# As of now, it only works with integers, float support will be added later





sinRegex = re.compile(r'(?:sin\(\-*\d*\))')
cosRegex = re.compile(r'(?:cos\(\-*\d*\))')
cRegex = re.compile(r'(?<=\()(\-*\d+(?:\+|\-|\/|\*)\-*\d+)+(?=\))')

def parseEqu(s):

    _local_string = str(s)

    print("Input String: " + _local_string)

    # Compute functions with values
    while True:
       
        if sinRegex.findall(_local_string):
            #print("checkpoint_1")
            matc = sinRegex.findall(_local_string)
            for matches in matc:
                ev = str(-1)
                _local_string = _local_string.replace(matches, ev)
            #print("(SIN) Handling match: " + str(matc))
            print("SIN changed string to -- " + _local_string)


        elif cosRegex.findall(_local_string):
            #print("checkpoint_2")
            matc = cosRegex.findall(_local_string)
            for matches in matc:
                ev = str(-10)
                _local_string = _local_string.replace(matches, ev)
            #print("(COS) Handling match: " + str(matc))
            print("COS changed string to -- " + _local_string)

        elif cRegex.findall(_local_string):
            #print("checkpoint_3")
            matc = cRegex.findall(_local_string)
            for matches in matc:
                ev = str(eval(matches))
                _local_string = _local_string.replace(matches, ev)
            #print("Literal Handling match: " + str(matc))
            print("Literal changed string to -- " + _local_string)

        else:
            break
    return str(eval(_local_string))



#string = 'sin(cos(22)+2232)-(1+1)*cos(100)'
string = '(((sin(22)+cos(332))*2+cos(cos(932)))/5)/sin(666)'
print('Final Answer: ' + parseEqu(string))
#print(eval("-10+-2232"))

# Use python's internal parser to parse the simple things (+, -, /, *, ())
