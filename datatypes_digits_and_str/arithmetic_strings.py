'''
Introduced 3 lines in random order. Write a program that finds out whether an arithmetic
progression can be constructed from the lengths of these strings.

Input format
The program is given three lines as input, each on a separate line.

Output format
The program should output the line “YES” if an arithmetic progression can be constructed from the
lengths of the entered words, or “NO” otherwise.
'''
a, b, c = input(), input(), input() #required lines
k = len(a) #found len of these strings
d = len(b)
e = len(c)
#is this ariphmeric progression based on them length or no
if (((max(k, d, e) + min(k, d, e)) / 2)  == (k + d + e - max(k, d, e) - min(k, d, e))):
   print("YES")
else:
   print("NO")