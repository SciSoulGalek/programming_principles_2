"""
Create a generator that generates the squares of numbers up to some number "N".
"""
def squares(limit):
    a = 1
    while a <= limit:
        yield a ** 2
        a += 1

x = int(input("Enter a number to get sequence of squares:\n"))

sequence = [str(square) for square in squares(x)]

print(f"Squares sequence up to {x}:\n{', '.join(sequence)}")