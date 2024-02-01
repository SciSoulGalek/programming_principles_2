"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Note: don't use collection set.
"""
def unique_list(numbers_list):
    new_list = []
    for i in range(len(numbers_list)):
        if(numbers_list[i] in new_list):
            continue
        else:
            new_list.append(numbers_list[i])
    return new_list

numbers_list = []
x = input("Enter numbers separated by space: ")

numbers_str = x.split()
numbers_list = [int(num_str) for num_str in numbers_str]

print("Unique elements in list:",unique_list(numbers_list))