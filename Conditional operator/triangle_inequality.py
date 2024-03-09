'''
Write a program that takes three positive numbers and determines whether a non-degenerate triangle with those sides exists.

Input format
The program is given three positive integers as input.

Output format
The program should output “YES” or “NO” in accordance with the condition of the problem.
'''
a = int(input())
b = int(input())
c = int(input())  #sides of triangle
if a + b > c and a + c > b and c + b > a: #degenerate or non-degenerate triangle
  print("YES")
else:
  print("NO")