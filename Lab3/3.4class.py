"""
Write the definition of a Point class. Objects from this class should have a:
a method "show" to display the coordinates of the point
a method "move" to change these coordinates
a method "dist" that computes the distance between 2 points
"""

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of point{self.name} are:", self.x, self.y)
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Coordinates of point{self.name} are changed to:", new_x, new_y)

    def dist(self, other_point):
        return(((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5)

point1 = Point(1, 1, 2)
point2 = Point(2, 4, 6)

point1.show()
point2.show()

print("Distance between two points is:", point1.dist(point2))

point1.move(7, 9)

print("Distance between two points is:", point1.dist(point2))