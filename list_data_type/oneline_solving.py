"""
The input to the program is a text string containing integers. Write a program that uses a list
expression to print squares of even numbers that do not end in 4.

Input format
The input to the program is a text string containing integers separated by a space character.

Output format
The program should output the text in accordance with the conditions of the task.

Note 1: The program can be written in one line of code.

Note 2. It is the squares of numbers that should not end with the number 4, and not the numbers themselves.
"""

# one line print squares of even numbers that do not end in 4
print(*[int(el) ** 2 for el in input().split() if int(el) % 2 == 0 and int(el) ** 2 % 10 != 4])
