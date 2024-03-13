'''
Given a natural number n. Write a program that prints a numerical triangle with height equal to n, following the example:

1
121
12321
1234321
123454321
...

Input format
The program is given one natural number as input.

Output format
The program should output a triangle according to the condition.

Note. Use a nested for loop.
'''
n = int(input()) #natural number n
for i in range(1, n + 1): #number of lines
  for j in range(1, i + 1): # 123..., "i" is the length of the string
    print(j, end="")
  for k in range(i - 1, 0, -1):  # ...321
     print(k, end="")
  print() #for starting new line
