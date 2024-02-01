"""
Define a class which has at least two methods: "getString:" to get a string from console input "printString:" to print the string in upper case.
"""
class string_manip:
    def getString(self):
        return input("Enter a string: ")

    def printString(self, s):
        print("You entered:", s.upper())

strings = string_manip() 
user_input = strings.getString()
strings.printString(user_input)