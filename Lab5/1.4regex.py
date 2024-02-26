"""
Write a Python program to find the sequences of one upper case letter followed by lower case letters.
"""
import re
pattern = '[A-Z][a-z]+'
output = re.findall(pattern, 'abcdefGhijklMnopqrStuvwxyz')
print(output)