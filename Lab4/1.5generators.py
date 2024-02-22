"""
Implement a generator that returns all numbers from (n) down to 0.
"""
def decreasing(start):
    while start >= 0:
        yield start
        start -= 1

x = int(input("Enter a number to get sequence of numbers from n to 0 (n must be a positive integer):\n"))

sequence = [str(num) for num in decreasing(x)]

print(f"Decreasing sequence from {x} up to 0:\n{', '.join(sequence)}")