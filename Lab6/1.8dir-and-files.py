"""
Write a Python program to delete file by specified path.
Before deleting check for access and whether a given path exists or not.
"""
import os
if os.path.exists("Lab6/1.8demofile.txt"):
    os.remove("Lab6/1.8demofile.txt")
else:
    print("The file does not exist")