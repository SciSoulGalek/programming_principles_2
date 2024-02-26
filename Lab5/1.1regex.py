"""
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""
import re
pattern = 'a[b]*'
output = re.findall(pattern, 'abcdefghijklmnopqrstuvwxyzabbbbbbbbbbb')
print(output)