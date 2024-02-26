"""
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
"""
import re
pattern = 'a.*?b'
output = re.findall(pattern, 'acdefghijklmnobacdefghijklbmnopqrstuvwxyzapqrstuvwxyzb')
print(output)

# output: 'acdefghijklmnob', 'acdefghijklb', 'apqrstuvwxyzb'