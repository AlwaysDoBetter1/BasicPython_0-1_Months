'''
Write a program that reads two integers and a symbol from the keyboard.
If this string is denoted by one of the four mathematical operations (+, -, *, /),
then the result will be that you enter the application of that operation to the previous numbers given,
otherwise you will enter "Invalid operation" (without the quotes). If the user wants to share zero,
you should write “Cannot share with zero!” (without quotes).

Input format
The input to the program is two integers and strings, all in a string string.

Output format
The program should output the result of applying the operation to the entered numbers or corresponding text
if the operation is invalid or if division by zero occurs.
'''
a, b = int(input()), int(input()) #nums
s = input() #symbol of operaton
if s == '+': #operations
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('Cannot share with zero!')
    else:
        print(a / b)
else: #if symbol not correct
    print('Invalid operation')