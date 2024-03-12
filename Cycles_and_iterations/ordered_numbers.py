'''
A natural number is given. Write a program that determines whether the sequence of its digits,
when viewed from right to left, is ordered in non-decreasing order.

Input format
The program is given one natural number as input.

Output format
The program should output "YES" if the sequence of its digits when viewed from right to left
is ordered in non-decreasing order and "NO" otherwise.
'''
n = int(input())  # required nums
flag = True

last_digit = n % 10  # for starting iteration
while n > 0:
    if last_digit > n % 10:  # if digit lesser than left digit - false
        flag = False
        break  # if flag false - we dont need next checking

    last_digit = n % 10  # next digits checking in sequence
    n //= 10

if flag:  # rezult
    print("YES")
else:
    print("NO")
