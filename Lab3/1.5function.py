"""
Write a function that accepts string from user and print all permutations of that string.
"""
from itertools import permutations

string = str(input())
all_permutations = permutations(string)

for perm in all_permutations:
    perm_str = ''.join(perm)
    print(perm_str)