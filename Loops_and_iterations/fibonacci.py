'''
Write a program that reads a natural number n and prints the first n numbers in the Fibonacci sequence.

Input format
The input of the program is one number n (n≤100) – the number of steps in the sequence.

Output format
The program should output the members of the Fibonacci sequence separated by spaces.

Note. According to the chronology of natural numbers, where each subsequent number is the sum of the previous two.
'''
a = 1 #first nums
b = 1 #second nums
h = int(input()) #len fibonacci
for i in range(h):
  if i < 2: #constant nums
    a = 1
  else: #printing fibonacci growth afrer 1, 1
    b, a = a, (a + b)
  print(a, end=" ") #printing only a, because b for growth working