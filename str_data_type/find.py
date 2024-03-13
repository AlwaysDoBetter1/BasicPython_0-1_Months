"""
A line of text is given as input to the program. If the letter “f” appears only once in this line, print its index.
If it occurs two or more times, print the indices of its first and last occurrence on the same line, separated
by a space character. If the letter "f" does not appear in this line, "NO" should be printed.

Input format
A line of text is given as input to the program.

Output format
The program should output the text in accordance with the conditions of the task.
"""

string = input()  # line for checking
if string.count("f") == 1:  # if "f" only one
    print(string.find("f"))
elif string.count("f") == 0:  # if "f" not founded
    print("NO")
else:  # if 2 and more "f" in line: print first and last "f" indexs
    print(string.find("f"), string.rfind("f"))
