'''
A regular polygon is a convex polygon in which all sides and all angles between adjacent sides are equal.
Area of a regular polygon with side length a and number of sides n is calculated using the formula:
S= n*a^2/(4tg(π/n))
Given two numbers: natural number n and real number a. Write a program that finds the area of a given regular polygon.

Input format
The program is given two numbers as input n and a, each on separate line.

Output format
The program should print a real number - the area of the polygon.
'''
from math import pi, tan
n, a = int(input()), float(input()) #required digits
print((n * a ** 2) / (4 * tan(pi / n))) #using formula from condition