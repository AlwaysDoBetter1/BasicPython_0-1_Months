"""
The input to the program is a text string containing integers. A list of numbers is formed from this string.
Write a program that counts how many pairs of elements in the resulting list are equal to each other.
It is believed that any two elements equal to each other form one pair that must be counted.

Input format
The input to the program is a text string containing integers separated by a space character.

Output format
The program should output one number - the number of pairs of elements equal to each other. And string of elements
"""

num, count = input().split(), 0

for i in range(len(num)):
    for j in range(i + 1, len(num)):  # Check for equality of all elements only from the element index to eliminate
        # duplicate elements
        if num[i] == num[j]:  # if any element has duplicate
            count += 1

print(count)
print(" ".join(num))  # string of elements
