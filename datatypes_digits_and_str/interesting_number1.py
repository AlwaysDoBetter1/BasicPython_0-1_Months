'''
Let's call a number interesting if the difference between the maximum and minimum digits
is equal to the average digit. Write a program that determines whether a number is interesting or not.
If the number is interesting, you should output “Number interesting”, otherwise - “Number uninteresting”.

Input format
The input to the program is a three-digit integer number.

Output format
The program should output the text in accordance with the conditions of the task.
'''
a = int(input()) #required num
l = abs(a // 100) #separate three digits
k = abs(a % 10)
e = abs((a // 10) % 10)
#conditional operation maximum - minimum digits == average digit
if (max(l, k, e) - min(l, k, e) == (l + k + e) - max(l, k, e) - min(l, k, e)):
   print("Number interesting")
else:
   print("Number uninteresting")