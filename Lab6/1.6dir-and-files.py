"""
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
"""
import string
import os

path = 'Lab6/1.6A-Z'

file_names = [os.path.join(path, f"{letter}.txt") for letter in string.ascii_uppercase]

for file_name in file_names:
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            pass
    else:
        print(f"File '{file_name}' already exists. Skipping creation.")

print("Files created or skipped successfully.")