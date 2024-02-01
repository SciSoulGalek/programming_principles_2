"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


numbers_list = []
print("This code checks for two consecutive 3s")
x = input("Enter numbers separated by space: ")


numbers_str = x.split()
numbers_list = [int(num_str) for num_str in numbers_str]

print(has_33(numbers_list))    
    