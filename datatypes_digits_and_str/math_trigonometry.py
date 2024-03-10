'''
Write a program to calculate the value of a trigonometric expression
sin(x)+cos(x)+tan^2(x) over a given number of degrees x

Input format
The input to the program is one real number x measured in degrees.

Output format
The program should output one number - the value of a trigonometric expression.

Note 1: Trigonometric functions take arguments in radians.
'''
import math
x = float(input()) #number x measured in degrees
x = math.radians(x) #convert to radians for math trigonometric functions
print(math.sin(x) + math.cos(x) + (math.tan(x)) ** 2) #found the value of a trigonometric expression