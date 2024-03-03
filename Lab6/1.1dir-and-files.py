"""
Write a Python program to list only directories, files and all directories, files in a specified path.
"""
import os

def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

path = input("Enter the path: ")
list_directories_files(path)

#Example of directory: c:\Users\galek\Documents\programming_principles_2\Lab6 