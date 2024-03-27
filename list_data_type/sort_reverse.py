"""
The input to the program is a text string containing integers. A list of numbers is formed from this string.
Write a program that counts how many pairs of elements in the resulting list are equal to each other.
It is believed that any two elements equal to each other form one pair that must be counted.

Input format
The input to the program is a text string containing integers separated by a space character.

Output format
The program should output one number - the number of pairs of elements equal to each other. And string of elements
"""

seq = []
for el in input().split():   # getting to str of digits which separated "space" and split them
    seq.append(int(el))  # add to list for sorting

seq.sort()  # sort list n...0
print(*seq)  # print as str

seq.reverse()  # 0...n
print(*seq)  # print as str
