'''
Please review that code because it so slowly
code: a problem that tests a number for primality
'''
# first version
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Prime number')
else:
    print('Composite number')

# 4000 times faster if num = 1934234249 and breaked if is the number is composite,
# and we have found its first divisor (other than 1)
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break
if num > 1 and flag == True:
    print('Prime number')
else:
    print('Composite number')