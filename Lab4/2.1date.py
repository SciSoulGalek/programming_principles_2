"""
Write a Python program to subtract five days from current date.
"""
import datetime
x = datetime.date.today() - datetime.timedelta(days = 5)
print(x)