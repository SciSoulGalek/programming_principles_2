"""
Define a function histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""
def histogram(numbers_list):
    for i in range(len(numbers_list)):
        print("*" * numbers_list[i])

numbers_list = []
x = input("Enter numbers separated by space: ")

numbers_str = x.split()
numbers_list = [int(num_str) for num_str in numbers_str]

histogram(numbers_list)
