"""
function that returns something
"""

# function declaration
def merge(list1, list2):  # merge 2 lists into 1
    list1.extend(list2)
    list1.sort()
    return list1  # return list

# read the data
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# call the function
print(merge(numbers1, numbers2))
