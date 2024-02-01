"""
Write a function that computes the volume of a sphere given its radius.
"""
def volume(radius):
    return radius**3 * 4 / 3

x = float(input("Radius of a sphere: "))

print(f"Volume of a sphere is {volume(x)}pi")