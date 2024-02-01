"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def has_007(numbers_list):
    zero_count = 0
    for i in range(len(numbers_list)):
        if numbers_list[i] == 0:
            zero_count += 1
        if zero_count >= 2 and numbers_list[i] == 7:
            return True
    return False
            
                
numbers_list = []
x = input("Enter numbers separated by space: ")

numbers_str = x.split()
numbers_list = [int(num_str) for num_str in numbers_str]

print(has_007(numbers_list))