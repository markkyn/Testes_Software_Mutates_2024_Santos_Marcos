import re
import ast


# (((Sin(22) + Cos(332)) * 2 + Cos(Cos(932))) / 5)/ Sin(666)
"""
fnc(#)+#
(fnc(#)+#)
fnc(fnc(#) + #)



"""
# As of now, it only works with integers, float support will be added later





sinRegex = re.compile(r'(?:sin\(\d*\))')
cosRegex = re.compile(r'(?:cos\(\d*\))')
cRegex = re.compile(r'\((.*?)\)')







priorityRegex = re.compile(r'(?<=\()(.*?)(?=\))')
literalRegex = re.compile(r'^[0-9]*$')

def parseEqu(s):

    _local_string = str(s)

    print("Input String: " + _local_string)

    # Compute functions with values
    if sinRegex.findall(_local_string):
        print("checkpoint_1")
        matc = sinRegex.findall(_local_string)
        for matches in matc:
           _local_string = sinRegex.sub("-1", _local_string)
        _local_string = parseEqu(_local_string)
        print("(SIN) Handling match: " + str(matc))


    if cosRegex.findall(_local_string):
        print("checkpoint_2")
        matc = cosRegex.findall(_local_string)
        for matches in matc:
            _local_string = cosRegex.sub("-10", _local_string)
        _local_string = parseEqu(_local_string)
        print("(COS) Handling match: " + str(matc))
        print("COS changed string to -- " + _local_string)



    if cRegex.findall(_local_string):
        print("checkpoint_3")
        matc = cRegex.findall(_local_string)
        for matches in matc:
            _local_string = cosRegex.sub(str(_local_string , _local_string))
        _local_string = parseEqu(_local_string)
        print("(COS) Handling match: " + str(matc))
        print("COS changed string to -- " + _local_string)




    """
    # Compute 'priority' parenthesis
    if priorityRegex.findall(_local_string):
        print("checkpoint_3")
        matc = priorityRegex.findall(_local_string)
        for matches in matc:
            _local_string = _local_string.replace(matches, parseEqu(matches))
        print("(Paren) Handling match: " + str(matc.groups()))


    
    # Compute basic operators
    else:

        # Check if the input is just a value
        if literalRegex.match(_local_string):
            print("checkpoint_4")
            print("Literal: " + _local_string + " found!")
            return _local_string
            
        else:
            print("checkpoint_5")

            # Split the equation at + or -
            if ('+' in _local_string) or ('-' in _local_string):
                Equsplit = re.compile(r'[\-\+]').split(_local_string)
            elif ('*' in _local_string) or ('/' in _local_string):
                # Split the equation at * or /
                Equsplit = re.compile(r'[\*\/]').split(_local_string)
            else:
                print("Something is wrong!")

            Operatorpos = len(Equsplit[0])
            print("Pos: " + str(Operatorpos))
            Leftelement = _local_string[:Operatorpos]
            print(Leftelement)
            Rightelement = _local_string[Operatorpos+1:]
            print(Rightelement)
            op = _local_string[Operatorpos]
            print(op)

            debug = 0
            if op == '+':
                debug = str(float(parseEqu(Leftelement)) + float(parseEqu(Rightelement)))
                return debug
            elif op == '-':
                debug = str(float(parseEqu(Leftelement)) - float(parseEqu(Rightelement)))
                return debug
            elif op == '*':
                debug = str(float(parseEqu(Leftelement)) * float(parseEqu(Rightelement)))
                return debug
            elif op == '/':
                denom = str(float(parseEqu(Rightelement)))
                # Validate denominator
                if denom == 0 or denom == None:
                    return None
                else:
                    return str(float(parseEqu(Leftelement)) / float(parseEqu(Rightelement)))
    """
    return _local_string



string = 'sin(cos(22)+2232)-(1+1)*cos(100)'
#print(parseEqu(string))
print(eval("1+1"))

# Use python's internal parser to parse the simple things (+, -, /, *, ())


