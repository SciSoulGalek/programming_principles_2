"""
Write a Python program that invoke square root function after specific milliseconds.
"""
import time
num = float(input('Number: '))
delay = float(input('Delay in miliseconds: '))
time.sleep(delay / 1000)
print(f'Square root of {num} after {delay} miliseconds is {num ** 0.5}')