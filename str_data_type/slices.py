"""
One line is given as input to the program. Write a program that prints:

third character of this line;
penultimate character of this line;
the first five characters of this line;
the entire line except the last two characters;
all symbols with even indexes;
all characters with odd indexes;
all characters in reverse order;
all characters of the string one after another in reverse order, starting from the last one.

Input format
The input to the program is one line, the length of which is more than 5 characters.

Output format
The program must output data according to the condition. Each value is displayed on a separate line.
"""

string = input()

# Third character of the line
print(string[2])

# Penultimate character of the line
print(string[-2])

# First five characters of the line
print(string[:5])

# Entire line except last two characters
print(string[:-2])

# All characters with even indexes
print(string[::2])

# All characters with odd indexes
print(string[1::2])

# All characters in reverse order
print(string[::-1])

# All characters of the string one after another in reverse order, starting with the last one
print(string[::-1][::2]) # or you can do this: print(string[::-2])