"""
Write a Python program to test whether a given path exists or not.
If the path exist find the filename and directory portion of the given path.
"""
import os
def path_info(path):
    if os.path.exists(path):
        lastSlashId = path.rfind('/')
        if lastSlashId != -1:
            directory = path[:lastSlashId]
            filename = path[lastSlashId + 1:]
        else:
            directory = ''
            filename = path
        return True, filename, directory
    else:
        return False, None, None
path = 'Lab6/lorem-ipsum.txt'
exists, filename, directory = path_info(path)
if exists:
    print(f"The path '{path}' exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print(f"The path '{path}' does not exist.")
