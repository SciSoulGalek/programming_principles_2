"""
Define a class named "Rectangle" which inherits from "Shape" class from task 2.
Class instance can be constructed by a "length" and "width".
The "Rectangle" class has a method which can compute the "area".
"""
class Shape:
    def area():
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        print(self.lenght * self.width)

s1 = Square(5)
s1.area()

s2 = Rectangle(3,7)
s2.area()

