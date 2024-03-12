'''
The program input is a natural number n. Write a program that prints numbers from 1 to n inclusive except:
-numbers from 5 to 9 inclusive;
-numbers from 17 to 37 inclusive;
-numbers from 78 to 87 inclusive.

Input format
The input to the program is one natural number n.

Output format
The program must output numbers in accordance with the problem conditions, each on a separate line.
'''
n = int(input())  #n
for i in range(1, n + 1): #checking exception
  if (5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87):
     continue #if exception - not print
  print(i)
