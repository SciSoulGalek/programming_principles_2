"""
Write a python program to convert snake case string to camel case string.
"""
import re
sample = 'abc_defghi_jklmno_pqrstu_vwxyz'
output = re.sub('_([a-zA-Z])', lambda x: x.group(1).upper(), sample)
print(output)

"""
Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"
"""