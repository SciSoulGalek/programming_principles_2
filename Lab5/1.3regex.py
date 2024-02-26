"""
Write a Python program to find sequences of lowercase letters joined with a underscore.
"""
import re
pattern = '[a-z]+_[a-z]+'
output = re.findall(pattern, 'abc_defghijklmn_opqrstu_vwxyz')
print(output)