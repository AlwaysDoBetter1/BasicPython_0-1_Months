'''
Given an odd natural number n. Write a program that prints an isosceles star triangle with base n as shown in the example:
*
**
***
****
***
**
*

Input format
The input to the program is one odd natural number.

Output format
The program should output a triangle according to the condition.
'''
n = int(input())  # required odd natural number

for i in range(n):  # number is odd
    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)  # if i > n // 2, cur_cnt starts decreasing
    for j in range(cur_cnt):  # we can just "*" * cur_cnt, but еhe problem explores the topic of nested loops
        # and I tried to solve it using them
        print("*", end="")
    print()
