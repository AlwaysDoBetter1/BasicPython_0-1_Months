'''
Given two natural numbers
m and n (m≤n). Write a program that prints all integers from m to n inclusive that
satisfy at least one of the following conditions:
-the number is a multiple of 17;
-the number ends in 9;
-number is a multiple of 3 and 5 at the same time.
Input format
The input to the program is two natural numbers m and n (m≤n), each on a separate line.

Output format
The program must output numbers in accordance with the conditions of the problem.

Note. If there are no numbers that satisfy the condition, there is no need to output anything.
'''
m, n = int(input()), int(input())  #m<=n

for i in range(m, n + 1): # |m, n|
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0: #if any number meets the condition -> print them
        print(i)