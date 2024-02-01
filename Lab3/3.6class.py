"""
Write a program which can filter prime numbers in a list by using "filter" function.
Note: Use lambda to define anonymous functions.
"""
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
numbers_list = []
x = input("Enter numbers separated by space: ")

numbers_str = x.split()
numbers_list = [int(num_str) for num_str in numbers_str]   

print(list(filter(lambda x : is_prime(x), numbers_list)))