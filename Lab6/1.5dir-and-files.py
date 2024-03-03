"""
Write a Python program to write a list to a file.
"""
list = ['George', 'Jonathan', 'Jorge', 'Joseph', 'Jotaro', 'Josuke', 'Giorno', 'Jolyne', 'Johnny', 'Gappy', 'Jodio']

try:
    with open('Lab6/1.5Joestars.txt', 'w') as f:
        f.write(', '.join(list) )
        print("List was written to the file")
except:
    print("Something went wrong")