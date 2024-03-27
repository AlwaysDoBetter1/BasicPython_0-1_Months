"""
Complete the given code so that it:

1. Replaced the second element of the list with 17;
2. Added numbers 4, 5 and 6 to the end of the list;
3. Removed the first element of the list;
4. Doubled the list;
5. Inserted the number 25 at index 3;
6. Printed a list using the print() function
"""

numbers = [8, 9, 10, 11]  # this code is started
# below is added extra code
numbers.remove(9)  # for replacement remove second element for point 1
numbers.insert(1, 17)  # insert to second place 17 for point 1
numbers.append(4)  # point 2
numbers.append(5)  # point 2
numbers.append(6)  # point 2
numbers.remove(8)  # point 3
numbers *= 2  # point 4
numbers.insert(3, 25)  # point 5
print(numbers)  # point 6
