"""
The input to the program is one number n. Write a program that prints a list of
n letters of the English alphabet ['a', 'b', 'c', ...] in lowercase.

Input format
The program input is a natural number n, 1 ≤ n ≤ 26.

Output format
The program should output the text in accordance with the conditions of the task.
"""

n = int(input())  # natural number n

s = ""  # for appending n letters
for i in range(n):
    s += chr(ord("a") + i)  # from "a" to n-letter append to s

print(list(s))  # convert str of n letters to list
