"""
Write a Python program to count the number of lines in a text file.
"""
def count_non_empty_lines(lines):
    non_empty_lines = sum(1 for line in lines if line.strip())
    return non_empty_lines

with open('Lab6/lorem-ipsum.txt', 'r') as file:
    lines = file.readlines()

non_empty_line_count = count_non_empty_lines(lines)
print(f"Number of non empty lines: {non_empty_line_count}")