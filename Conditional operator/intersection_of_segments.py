'''
Two segments are given on a number line: [a, b] and [c, d] Write a program that finds their intersection.
The intersection of two segments can be:
-line segment;
-dot;
-empty set.

Input format
Upon entering the program is presented 4 integers a1, b1, a2, b2, each on a separate line. It is guaranteed that a1<b1 and a2<b2

Output format
The program should display the boundaries of the segment that is the intersection, or a common point, or the text “empty set”.
'''
a, b, c, d = int(input()), int(input()), int(input()), int(input()) #a, b - first line; c, d - second line
if a < c:  #finding intersection
   amax = c
else:
   amax = a
if b < d:
   bmin = b
else:
   bmin = d
if amax > bmin:
   print("empty set")
elif amax == bmin:
   print(amax)
else:
   print(amax, bmin)