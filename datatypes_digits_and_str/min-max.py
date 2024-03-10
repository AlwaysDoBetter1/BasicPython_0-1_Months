'''
Write a program that orders three numbers from largest to smallest.(use only min-max)

Input format
The input program offers three integers, each on a separate line.

Output format
The program should print three numbers, each on a separate line, ordered from largest to smallest.
'''
a, b, s = int(input()), int(input()), int(input())  #required numbers
print(max(a, b, s)) #first
print((a + b + s) - min(a, b, s) - max(a, b, s)) #second numbers
print(min(a, b, s)) #last