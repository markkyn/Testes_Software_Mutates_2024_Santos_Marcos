import re

# (((Sin(22) + Cos(332)) * 2 + Cos(Cos(932))) / 5)/ Sin(666)
# As of now, it only works with integers, float support will be added later





sinRegex = re.compile(r'(?:sin\(\d*\))')
cosRegex = re.compile(r'(?:cos\(\d*\))')
priorityRegex = re.compile(r'(?<!^sin)(?<!^cos)(\(.*?\))')
literalRegex = re.compile(r'^[0-9]*$')

def parseEqu(s):

    print("Input String: " + s)

    # Compute functions with values
    if sinRegex.match(s):
        print("checkpoint_1")
        matc = sinRegex.search(s)
        print("(SIN) Handling match: " + matc.group())
        return "-1"
        pass 
    elif cosRegex.match(s):
        print("checkpoint_2")
        matc = cosRegex.search(s)
        print("(COS) Handling match: " + matc.group())
        return "-10"
        pass

    # Compute 'priority' parenthesis
    elif priorityRegex.match(s):
        print("checkpoint_3")
        matc = priorityRegex.search(s)
        print("(Paren) Handling match: " + matc.group())
        parseEqu(matc.group()[1:-1])
        pass

    # Compute basic operators
    else:

        # Check if the input is just a value
        if re.match(r'^[0-9]*$', s):
            print("checkpoint_4")
            print("Literal: " + s + " found!")
            return s
            
        else:
            print("checkpoint_5")
            # Split the equation at + or -
            if ('+' in s) or ('-' in s):
                Equsplit = re.compile(r'[\-\+]').split(s)
            elif ('*' in s) or ('/' in s):
                # Split the equation at * or /
                Equsplit = re.compile(r'[\*\/]').split(s)
            else:
                pass

            Operatorpos = len(Equsplit[0])
            print("Pos: " + str(Operatorpos))
            Leftelement = s[:Operatorpos]
            print(Leftelement)
            Rightelement = s[Operatorpos+1:]
            print(Rightelement)
            op = s[Operatorpos]
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



string = 'sin(2232)-(1+1)'
parseEqu(string)


