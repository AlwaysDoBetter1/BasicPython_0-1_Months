'''
Write a program that reads three numbers and calculates the sum of only positive numbers.

Input format
The program receives three integers as input.

Output format
The program should output one number - the sum of positive numbers.
'''
a, b, c = int(input()), int(input()), int(input()) #requried three numbers for sum
if a < 0: #if any number less than 0 - number nullified for disabling in sum
  a = 0
if b < 0:
  b = 0
if c < 0:
  c = 0
print(a + b + c)