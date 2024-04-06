"""
The input to the program is a natural number in the decimal number system. Write a program that converts it into binary,
octal and hexadecimal number systems.
"""

a = int(input())
print(bin(a)[2:])
print(oct(a)[2:])
print(hex(a)[2:].upper())
