"""
The input to the program is a natural number n, and then n integers.
Write a program that first prints all negative numbers, then zeros, and then all positive numbers,
each on a separate line. The numbers must be output in the same order in which they were entered.

Input format
The input to the program is a natural number n, and then n integers, each on a separate line.

Output format
The program should output the text in accordance with the conditions of the task.
"""

negatives, zeros, positives = [], [], []

n = int(input())
for _ in range(n):
    cur = int(input())
    if cur < 0:
        negatives.append(cur)  # all negative numbers
    elif cur > 0:
        positives.append(cur)  # all positive numbers
    else:
        zeros.append(cur)  # all zeros

res = negatives + zeros + positives  # concatenate lists for easier working with them
print(*res, sep="\n")
