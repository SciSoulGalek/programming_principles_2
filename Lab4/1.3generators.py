"""
Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
"""
def divisibles(limit):
    a = 1
    while a <= limit:
        if a % 3 == 0 or a % 4 == 0:
            yield a
        a += 1

limit = int(input("Enter a number to get sequence of numbers divisible by 3 and 4:\n"))

sequence = [str(div) for div in divisibles(limit)]

print(f"Sequence of numbers divisible by 3 and 4 from 0 up to {limit}:\n{', '.join(sequence)}")