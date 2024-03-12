'''
The input to the program is a sequence of words, each word on a separate line.
The end of the sequence is the word "END" or "end" (in capital or small letters, without quotes).
Moreover, the words “END” and “end” themselves are not included in the sequence, only symbolizing its ending.
Write a program that prints the members of a given sequence.

Input format
The input to the program is a sequence of words, each word on a separate line.

Output format
The program must print the members of the given sequence.
'''
a = input() #first input for starting iteration
while (a != "END") and (a != "end"): #if a == end -> stop iteration
  print(a)
  a = input() #next step iteration