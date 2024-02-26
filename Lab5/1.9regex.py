"""
Write a Python program to insert spaces between words starting with capital letters.
"""
import re
sample = 'abcDefghiJklmnoPqrstuVwxyz'
output = re.sub('(?<=[a-z])(?=[A-Z])', ' ', sample)
print(output)