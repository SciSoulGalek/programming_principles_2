"""
Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
"""
import re
pattern = 'a[b]{2,3}'
output = re.findall(pattern, 'abbbabcdefghijklmnopqrstuvwxyzabb')
print(output)