"""
Write a function that accepts string from user and print all permutations of that string.
"""
from itertools import permutations

def permutation(string):
    all_permutations = permutations(string)
    for perm in all_permutations:
        perm_str = ''.join(perm)
        print(perm_str)

string = str(input())
permutation(string)