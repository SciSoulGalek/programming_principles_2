"""
Implement a generator called squares to yield the square of all numbers from (a) to (b).
Test it with a "for" loop and print each of the yielded values.
"""
def squares(start, end):
    current = start
    while current <= end:
        yield current ** 2
        current += 1
        
for square in squares(1, 5):
    print(square)