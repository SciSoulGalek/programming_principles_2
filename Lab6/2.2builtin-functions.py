"""
Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters.
"""
x = input()
uppers = 0
lowers = 0
for i in range(len(x)):
    if x[i].isalpha():
        if x[i].isupper():
            uppers += 1
        else:
            lowers += 1
print(f'Number of upper case letters is {uppers} and lower case letters is {lowers}')