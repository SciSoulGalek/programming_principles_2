"""
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))


numbers_list = []
x = input("Enter numbers separated by space: ")


numbers_str = x.split()
numbers_list = [int(num_str) for num_str in numbers_str]


prime_numbers = filter_prime(numbers_list)

print(prime_numbers)