"""
Write a Python program to convert a given camel case string to snake case.
"""
import re
sample = 'abcDefghiJklmnoPqrstuVwxyz'
sample = re.sub('(?<=[a-z])(?=[A-Z])', '_', sample)
output = re.sub('([A-Z])', lambda x: x.group(1).lower(), sample)
print(output)

"""
Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"
"""