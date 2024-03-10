'''
Given three real numbers
a, b, c. Write a program that finds the real roots of a quadratic equation:

a(x^2)+b(x)+c=0.
If the equation has two steps, then they should be derived in ascending order.

Input format
Three real numbers are given as input to the program
a≠0,b,c, each on a separate line.

Output format
The program should print the Boolean equations for each individual line if they exist, or the text "No roots" otherwise.
'''
a = float(input())  #required nums
b = float(input())
c = float(input())
d = b**2-4*a*c #for check condition "No roots"

if d < 0: #checking condition "No roots"
    print('No roots')
elif d == 0: #if d == 0 only 1 solve exist
    print(-b / (2*a))
elif d > 0: #found 2 solvings required equation
    x1 = (-b - d ** 0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))