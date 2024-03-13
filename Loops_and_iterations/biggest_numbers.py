'''
The input to the program is a natural number n, and then n different natural numbers of the sequence,
each on a separate line. Write a program that prints the largest and second largest numbers in a sequence.
n >= 0
Input format
The input to the program is a natural number n≥2, and then n different natural numbers, each on a separate line.

Output format
The program should print the two largest numbers, each on a separate line.
'''
n = int(input())
max1, max2 = -1, -1  #if they > than once of them, once of them = num
for _ in range(n):
    num = int(input())
    if num > max1:
        max2 = max1 #second biggest = first biggest old count
        max1 = num #biggest number new count
    elif num > max2: #check for second biggest
        max2 = num

print(max1)
print(max2)