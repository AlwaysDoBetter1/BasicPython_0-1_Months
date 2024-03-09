'''
Write a program that, based on the user’s age entered, tells which age group he belongs to:

0-13 (inclusive) – childhood;
from 14 to 24 (inclusive) – youth;
from 25 to 59 (inclusive) – maturity;
from 60 (inclusive) – old age.
Input format
The program is given one integer as input – the user’s age.

Output format
The program should display the name of the age group.
'''
a = int(input()) # your age
if a <= 13: #your age group
  print("childhood")
else:
  if 14 <= a <= 24:
    print("youth")
  else:
    if 25 <= a <= 59:
      print("maturity")
    else:
      print("old age")