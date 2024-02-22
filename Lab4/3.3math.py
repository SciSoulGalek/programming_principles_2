"""
Write a Python program to calculate the area of regular polygon.
"""
import math
sides = int(input("Number of sides: "))
length = int(input("Length of side: ")) 
area = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
print(f"Area of regular polygon of {sides} with length {length} is {round(area, 10)}")