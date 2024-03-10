'''
Given five numbers a1, a2, a3, a4, a5. Write a program that calculates the sum of their modules

Input format
The program receives five real numbers as input. a1, a2, a3, a4, a5 each on a separate line.

Output format
The program should output one number - the sum of the modules of the entered numbers.
'''
a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input()) #numbers are real, not int
q = abs(a) + abs(b) + abs(c) + abs(d) + abs(e) #sum of their modules
print(q)