"""
Write a Python program to replace all occurrences of space, comma, or dot with a colon.
"""
import re
pattern = '[ .,]+'
sample = 'abc def.ghi,jkl mno.pqr,stu vwx.yz,'
output = re.sub(pattern, ':', sample)
print(output)
