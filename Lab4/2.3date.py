"""
Write a Python program to drop microseconds from datetime.
"""
import datetime
x = datetime.datetime.now().replace(microsecond = 0)
print("Datetime without microseconds: ", x)