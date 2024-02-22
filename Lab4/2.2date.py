"""
Write a Python program to print yesterday, today, tomorrow.
"""
import datetime
x = datetime.date.today()
print(f"Yesterday's date: {x - datetime.timedelta(days = 1)}")
print(f"Today's date: {x}")
print(f"Tomorrow's date: {x + datetime.timedelta(days = 1)}")
