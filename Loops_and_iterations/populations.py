'''
The program is given three natural numbers as input m,p,n:
m: starting number of organisms;
p: average daily increase in %;
n: number of days to reproduce.
Write a program that predicts the population size of organisms. The program should
print the population size for each day, starting from 1 and ending nth day.

Input format
The program is given three natural numbers as input.

Output format
The program should output the text in accordance with the conditions of the task.

Note. The problem is solved through compound interest.
'''
a, b, c = int(input()), int(input()), int(input()) # starting number of organisms and % their growth per day and days count
for i in range(c):
  print(i + 1, a * ((1 + b / 100) ** i)) #print day number and organizm populations in day