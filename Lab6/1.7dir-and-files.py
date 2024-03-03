"""
Write a Python program to copy the contents of a file to another file.
"""
with open('Lab6/1.5Joestars.txt', 'r') as source, open('Lab6/1.7copy+paste.txt', 'w') as destination:
    inf = source.read()
    destination.write(inf)