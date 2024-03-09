'''
Red, blue and yellow are called primary colors because they cannot be created by mixing other colors.
When two primary colors are mixed, a secondary color is obtained:

- if you mix red and blue, you get purple;
- if you mix red and yellow, you get orange;
- If you mix blue and yellow, you get green.
Write a program that reads the names of two primary colors to mix. If the user enters anything other than “red,”
“blue,” or “yellow,” the program should display an error message. Otherwise, the program should print the name
of the secondary color that will be the result.

Input format
The program receives two lines as input, each on a separate line.

Output format
The program should display the resulting mixture color or a “color error” message if the wrong color was entered.

Note: If you mix red and red, you get red, etc.
'''
a, b = input(), input()

if a == 'red' and b == 'blue' or a == 'blue' and b == 'red':
    print('purple')
elif a == 'red' and b == 'yellow' or a == 'yellow' and b == 'red':
    print('orange')
elif a == 'blue' and b == 'yellow' or a == 'yellow' and b == 'blue':
    print('green')
elif (a == 'blue' or a == 'red' or a == 'yellow') and a == b:
    print(a)
else:
    print('color error')