'''
Given two different squares of a chessboard. Write a program that determines whether a rook
can get from the first square to the second in one move. The program receives four numbers as input from
1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell.
The program should output “YES” if the rook can move from the first square to the second one, or “NO” otherwise.

Input format
The program is given four numbers as input from 1 to 8.

Output format
The program should output the text in accordance with the conditions of the task.
'''
a = int(input()) #starting rook
b = int(input()) #starting rook
c = int(input()) #ending rook
d = int(input()) #ending rook
if a == c and b == d: #perhaps the rook will go to the ending with 1 step
  print("NO")
elif a == c or b == d:
  print("YES")
else:
  print("NO")