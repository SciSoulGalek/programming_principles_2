"""
Write a program to solve a classic puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
create function: solve(numheads, numlegs):
"""
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    print(f"Rabbits: {int(rabbits)}")
    print(f"Chickens: {int(chickens)}")
x = int(input("Number of heads: "))
y = int(input("Number of legs: "))
solve(x, y)
 