"""
Write a function get_circle(radius) that takes the radius of a circle as an argument and returns
two values: the length of the circle and the area of the circle bounded by the given circle.
"""

# function declaration
def get_circle(radius):
    import math
    length = 2 * math.pi * r
    square = math.pi * r ** 2
    return length, square

# read the data
r = float(input())

# call the function
length, square = get_circle(r)
print(length, square)
