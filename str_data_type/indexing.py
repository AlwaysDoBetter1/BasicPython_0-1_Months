'''
One line is given as input to the program. Write a program that determines how many identical adjacent symbols it contains.

Input format
One line is given as input to the program.

Output format
The program should display the number of identical adjacent symbols.
'''
a = input()  # the line in which we will search for adjacent symbols
count = 0  # count of adjacent symbols
for i in range(0, len(a) - 1):  # iteration on the line
    if a[i] == a[i + 1]:  # if right symbol == left: count+=1
        count += 1
print(count)
