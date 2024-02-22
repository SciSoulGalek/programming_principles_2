"""
Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
"""
def evens(limit):
    a = 0
    while a <= limit:
        yield a
        a += 2

x = int(input("Enter a number to get sequence of evens:\n"))

sequence = [str(even) for even in evens(x)]

print(f"Evens sequence from 0 up to {x}:\n{', '.join(sequence)}")