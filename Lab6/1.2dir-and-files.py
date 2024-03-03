"""
Write a Python program to check for access to a specified path.
Test the existence, readability, writability and executability of the specified path.
"""
import os

def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    print(f"Path '{path}' exists.")

    if os.access(path, os.R_OK):
        print(f"Path '{path}' is readable.")
    else:
        print(f"Path '{path}' is not readable.")

    if os.access(path, os.W_OK):
        print(f"Path '{path}' is writable.")
    else:
        print(f"Path '{path}' is not writable.")

    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable.")
    else:
        print(f"Path '{path}' is not executable.")

path = input("Enter the path to check access: ")
check_path_access(path)