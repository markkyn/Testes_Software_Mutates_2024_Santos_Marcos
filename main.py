# import the ExponentialFunction class to use the ExponentialFunction
from ExponentialFunction import ExponentialFunction
# import array to use the array object


# Calculator class is the main class where user can choose the desired function
class Calculator:

    # Calculator has one parameter
    # history is an array object which stores history of functions used
    def __init__(self):
        print("Welcome to the Eternity System\n")
        self.history = ["History"]

    # The addition function is used to do simple addition
    def addition(self):
        # The values to be added are stored in an array named values
        values = []
        # num is the input from the user
        num = ""
        num = input("Enter value to be added, Enter '=' when all values "
                    "entered: ")
        # The user can enter as many values as they want
        # Once they've entered all their values, the user enters = to get the
        # answer
        while "=" not in num:
            values.append(float(num))
            num = input("Enter value to be added, Enter '=' when all values "
                        "entered: ")
        # sum is used to store the final answer, it is assigned the first value
        # in values
        # answer is used to store the work for the addition, which is later
        # stored in history
        sum = values[0]
        answer = str(sum)
        # The values entered are added, while the answer string is updated with
        # each value
        for i in range(1, len(values)):
            sum += values[i]
            answer = answer + " + " + str(values[i])
        answer = answer + " = " + str(sum)
        # The answer is then returned
        return answer

    # The subtraction function is used to do simple simple subtraction
    def subtraction(self):
        # The values to be subtracted are stored in an array
        values = []
        # num is the input from the user
        num = ""
        num = input("Enter value to be subtracted, Enter '=' when all values "
                    "entered: ")
        # The user can enter as many values as they want
        while "=" not in num:
            values.append(float(num))
            num = input("Enter value to be subtracted, Enter '=' when all "
                        "values entered: ")
        # diff is used to store the answer of the subtraction
        # It is assigned the first value of the array values
        diff = values[0]
        answer = str(diff)
        # The values entered are subtracted, while the answer string is updated
        # with each value
        for i in range(1, len(values)):
            diff -= values[i]
            answer = answer + " - " + str(values[i])
        answer = answer + " = " + str(diff)
        # The answer is then returned
        return answer

    def multiplication(self):
        # The values to be multiplied are stored in an array
        values = []
        # num is the input from the user
        num = ""
        num = input("Enter value to be multiplied, Enter '=' when all values "
                    "entered: ")
        # The user can enter as many values as they want
        while "=" not in num:
            values.append(float(num))
            num = input("Enter value to be multiplied, Enter '=' when all "
                        "values entered: ")
        # mult is used to store the answer of the multiplication
        # It is initally assigned the first value of the values array
        mult = values[0]
        answer = str(mult)
        # The values entered are multiplied, while the answer string is updated
        # with each value
        for i in range(1, len(values)):
            mult *= values[i]
            answer = answer + " x " + str(values[i])
        answer = answer + " = " + str(mult)
        # The answer is then returned
        return answer

    # The division function is used to do simple division
    def division(self):
        # The values to be divided are stored in an array
        values = []
        # num is the input from the user
        num = ""
        num = input("Enter value to be divided, Enter '=' when all values "
                    "entered: ")
        # The user can enter as many values as they want
        while "=" not in num:
            values.append(float(num))
            num = input("Enter value to be divided, Enter '=' when all values"
                        " entered: ")
        # div is used to store the answer of the division
        # It is initially assigned the first value of the values array
        div = values[0]
        answer = str(div)
        # The values entered are divided, while the answer string is updated
        # with each value
        for i in range(1, len(values)):
            # If the user tries to divide by zero, the function will exit
            try:
                div /= values[i]
                answer = answer + " / " + str(values[i])
            except ZeroDivisionError:
                print("Can't divide by zero, function will exit")
                self.choose_function(0)
        answer = answer + " = " + str(div)
        # The answer is then returned
        return answer

    # The parse_function method is used to perform two or more types of
    # operations
    # It has 2 paramters
    # current_result represents the current answer from the previous function
    # current_str represents the current string of the previous function
    def parse_function(self, current_result, current_str):
        # The user is first asked if they want to either add a function,
        # subtract a function, multiply a function, or divide a function
        print("Please choose one of the following choices: ")
        print("1. Add another function")
        print("2. Subtract another function")
        print("3. Multiply another function")
        print("4. Divide another function")
        parse = input("Enter the value of choice you would like: ")
        print()

        # If the user enters an invalid number, the system asks for another
        # input
        while (int(parse) < 1 or int(parse) > 4):
            parse = input("Invalid input, Please enter a new value: ")
            print()

        # The choose_function method is then called, this time using parse = 1
        # This way, it will return the result of the parsed function
        # Which will then be added to the current_value
        result = self.choose_function(1)

        # The result is returned as a string, so it is broken up into values
        # and answer
        new_values, new_answer = result.split(" = ")
        # The same for the current_str as well
        current_values, current_answer = current_str.split(" = ")

        # The values are then added based on the choice made for parse
        # If parse == 1, then the user wanted to add a new function
        if (int(parse) == 1):
            values = current_values + " + " + new_values
            answer = current_result + float(new_answer)
            # Function stores the new string for history
            function = values + " = " + str(answer)
            # The new value is displayed and the user is asked again if they
            # want to parse another function
            print(function)
            print()
            parseSecond = input("Would you like to parse another function "
                          "(Y or N) ")
            # If the user enters Y, then parse_function is called again with
            # the new answer
            if (parseSecond.casefold() == "Y".casefold()):
                self.parse_function(answer, function)
            # Else, the function is saved in history and choose_function is
            # called again
            else:
                self.history.append(function)
                self.choose_function(0)

        # The same thing is done for the choices of subtraction, multiplication
        # and division
        # If parse == 2, then the new fucntion is subtracted from the old
        elif (int(parse) == 2):
            values = current_values + " - " + new_values
            answer = current_result - float(new_answer)
            # Function stores the new string for history
            function = values + " = " + str(answer)
            # The new value is displayed and the user is asked again if they
            # want to parse another function
            print(function)
            print()
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            # If the user enters Y, then parse_function is called again with
            # the new answer
            if (parseSecond.casefold() == "Y".casefold()):
                self.parse_function(answer, function)
            # Else, the function is saved in history and choose_function is
            # called again
            else:
                self.history.append(function)
                self.choose_function(0)

        # If parse == 3, the new function is multiplied to the old one
        elif (int(parse) == 3):
            values = current_values + " x " + new_values
            answer = current_result * float(new_answer)
            # Function stores the new string for history
            function = values + " = " + str(answer)
            # The new value is displayed and the user is asked again if they
            # want to parse another function
            print(function)
            print()
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            # If the user enters Y, then parse_function is called again with
            # the new answer
            if (parseSecond.casefold() == "Y".casefold()):
                self.parse_function(answer, function)
            # Else, the function is saved in history and choose_function is
            # called again
            else:
                self.history.append(function)
                self.choose_function(0)

        # If parse == 4, the new function is divided to the old one
        else:
            values = current_values + " / " + new_values
            # Try to divide the values, but if it's divide by zero, catch
            # exception
            try:
                answer = current_result / float(new_answer)
            except ZeroDivisionError:
                print("Can't divide by zero, function will exit")
                self.choose_function(0)
            # Function stores the new string for history
            function = values + " = " + str(answer)
            # The new value is displayed and the user is asked again if they
            # want to parse another function
            print(function)
            print()
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            # If the user enters Y, then parse_function is called again with
            # the new answer
            if (parseSecond.casefold() == "Y".casefold()):
                self.parse_function(answer, function)
            # Else, the function is saved in history and choose_function is
            # called again
            else:
                self.history.append(function)
                self.choose_function(0)

    # choose_function method allows the user to choose which function to use
    # The user can choose one of the simple arithmetic functions, or the
    # special functions implemented
    # The second paramter is used when parsing a function
    # If parse = 0, then choose_function operates normally
    # If parse = 1, then choose_function returns the value of the chosen
    # fucntion
    # So it can then be parsed with a previously chosen function
    def choose_function(self, parse):
        print("Please choose one of the following functions")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Subtraction")
        print("5. arccos(x)")
        print("6. ab" + ExponentialFunction.get_super('x'))
        print("7. logb(x)")
        print("8. MAD (Mean Absolute Deviation)")
        print("9. σ (Standard Deviation)")
        print("10. sinh(x)")
        print("11. x" + ExponentialFunction.get_super('y'))
        print("12. Display History")
        print("13. Exit Calculator")

        choice = input("Enter the number of the function you would like to "
                       "use: ")
        print()

        # If the user enters an invalid number, it asks for input again
        while (int(choice) < 1 or int(choice) > 13):
            choice = input("Invalid input, Please enter a new value: ")
            print()

        # If the user enters 1, the addition function is called
        if (int(choice) == 1):
            result = self.addition()

            # If parse == 1, then choose_function returns the value of result
            if (parse == 1):
                return result

            # The user is then asked if they want to parse this function with
            # another
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            print()
            # If the user wants to parse a function, parse_function is called
            # and the answer of the previous function is taken from result
            if (parseSecond.casefold() == "Y".casefold()):
                values, answer = result.split("= ")
                self.parse_function(float(answer), result)

            # Else, the result is displayed
            else:
                print(result)
                self.history.append(result)
                input("Press Enter to continue:")
                print()
                self.choose_function(0)

        # If the user enters 2, the subtraction function is called
        # It follows the same format as the addition function, now using
        # subtraction
        elif (int(choice) == 2):
            result = self.subtraction()

            # If parse == 1, then choose_function returns the value of result
            if (parse == 1):
                return result

            # The user is then asked if they want to parse this function with
            # another
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            print()
            # If the user wants to parse a function, parse_function is called
            # and the answer of the previous function is taken from result
            if (parseSecond.casefold() == "Y".casefold()):
                values, answer = result.split("= ")
                self.parse_function(float(answer), result)

            # Else, the result is displayed
            else:
                print(result)
                self.history.append(result)
                input("Press Enter to continue:")
                print()
                self.choose_function(0)

        # If the user enters 3, the multiplication function is called
        elif (int(choice) == 3):
            result = self.multiplication()

            # If parse == 1, then choose_function returns the value of result
            if (parse == 1):
                return result

            # The user is then asked if they want to parse this function with
            # another
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            print()
            # If the user wants to parse a function, parse_function is called
            # and the answer of the previous function is taken from result
            if (parseSecond.casefold() == "Y".casefold()):
                values, answer = result.split("= ")
                self.parse_function(float(answer), result)

            # Else, the resukt is displayed
            else:
                print(result)
                self.history.append(result)
                input("Press Enter to continue:")
                print()
                self.choose_function(0)

        # If the user enters 4, the division function is called
        elif (int(choice) == 4):
            result = self.division()

            # If parse == 1, then choose_function returns the value of result
            if (parse == 1):
                return result

            # The user is then asked if they want to parse this function with
            # another
            parseSecond = input("Would you like to parse another function "
                          "(Y or N): ")
            print()
            # If the user wants to parse a function, parse_function is called
            # and the answer of the previous function is taken from result
            if (parseSecond.casefold() == "Y".casefold()):
                values, answer = result.split("= ")
                self.parse_function(float(answer), result)

            # Else, the resukt is displayed
            else:
                print(result)
                self.history.append(result)
                input("Press Enter to continue:")
                print()
                self.choose_function(0)

        # If the user enters 5, the arccos function is called
        elif (int(choice) == 5):
            exit()

        # If the user enters 6, the Exponential function is called
        elif (int(choice) == 6):
            function = ExponentialFunction(0, 0, 0, 0)

            # Display format of Exponential Function
            print('ab' + ExponentialFunction.get_super('x'))

            # Ask the user to input the value for a
            mNum = input("Enter value for a: ")
            check = function.set_mult_num(mNum)

            # Then ask the user to enter the value for b, and perform the same
            # checks
            bNum = input("Enter value for b: ")
            check = function.set_base_num(bNum)

            # Ask the user to enter the value for x
            eNum = input("Enter value for x: ")
            check = function.set_exp_num(eNum)

            # If any of the inputs were a fraction that resulted in a
            # ZeroDivisionError then check is equal to None and the function
            # stops
            if (check == None):
                print("ERROR Division by Zero\n")

            # Else, calculate the answer like normal
            else:
                result = function.calculate_answer()
                # If parse == 1, then choose_function returns the value of
                # result
                if (parse == 1):
                    return str(function)

                # The user is then asked if they want to parse this function
                # with another
                parseSecond = input("Would you like to parse another function "
                              "(Y or N): ")
                print()
                # If the user wants to parse a function, parse_function is called
                # and the answer of the previous function is taken from result
                if (parseSecond.casefold() == "Y".casefold()):
                    self.parse_function(result, str(function))

                # Else, the result is displayed
                else:
                    print(function)
                    self.history.append(str(function))

            input("Press Enter to continue:")
            print()
            self.choose_function(0)

        # If the user enters 7, log function is called
        elif (int(choice) == 7):
            exit()

        # If the user enters 8, the MAD function is called
        elif (int(choice) == 8):
            exit()

        # If the user enters 9, the Standard Deviation function is called
        elif (int(choice) == 9):
            exit()

        # If the user enters 10, the sinh function is called
        elif (int(choice) == 10):
            exit()

        # If the user enters 8, the x^y function is called
        elif (int(choice) == 11):
            exit()

        # If the user enters 12, the current history of the Calculator is displayed
        elif (int(choice) == 12):

            # If parse == 1, then the user should have chosen a function
            # choose_function is then called again
            if (parse == 1):
                print("Please choose a function to parse!")
                self.choose_function(1)

            for i in (self.history):
                print(i + "\n")
            input("Press Enter to continue:")
            self.choose_function(0)

        # If the user enters 13, the calculator exits
        else:
            print("Thank you for using the Eternity System. Goodbye")
            exit()


# Start with simple ExponentialFunction option where all values are 0
calculator = Calculator()
calculator.choose_function(0)
