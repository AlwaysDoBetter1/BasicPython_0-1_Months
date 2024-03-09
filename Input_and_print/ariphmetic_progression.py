'''
Input data:
The program is given three integers as input: a, d, n, each on a separate line.
a - starting digit
d - arithmetic progression difference
n - number of steps
Output:
The program should output n'th term of an arithmetic progression.
'''
a = int(input())
d = int(input())
n = int(input())  #required numbers
print(a + d * (n - 1)) #formula arithmetic progression