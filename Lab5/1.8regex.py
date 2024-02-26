"""
Write a Python program to split a string at uppercase letters.
"""
import re
pattern = '[A-Z]'
sample = 'abcDefghiJklmnoPqrstuVwxyz'
output = re.split(pattern, sample)
print(output)