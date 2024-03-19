"""
A natural number is given as input to the program
n and n lines, and then the number k. Write a program that prints the k'th letter of the input
strings on one line without spaces.

Input format
The input to the program is a natural number n, then n lines, each on a separate line.
At the end, enter the natural number k - the number of the letter (numbering starts from one).

Output format
The program should output the text in accordance with the conditions of the task.

Note. If some lines are too short and do not contain a character with a given number,
then such lines should be ignored in output.
"""

n = int(input())  # count of lines
li = []
for _ in range(n):
    li.append(input())  # build of list with n lines
k = int(input())  # for found k letter in each line
res = ''  # line with k letters in each string of li
for s in li:  # found of k letter in every line in list
    if len(s) >= k:
        res += s[k - 1]

print(res)
