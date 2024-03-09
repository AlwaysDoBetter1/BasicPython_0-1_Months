'''
Write a program to convert the value of a time interval specified in minutes into a value expressed in hours and minutes.

Input format
The input to the program is an integer - the number of minutes.

Output format
The program should output the text in accordance with the conditions of the task.
'''
minutes = int(input())  #total minutes
print(minutes, "minutes - this is", minutes // 60, "hours", minutes % 60, "minutes.")
#nuber of hours and minutes in total minutes