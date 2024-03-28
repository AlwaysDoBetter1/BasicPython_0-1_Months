"""
Write a function is_correct_bracket(text) that takes as an argument a non-empty string text consisting
of the characters ( and ) and returns True if the input string is a correct bracket sequence and False otherwise.

Note 1. A regular bracket sequence is a string consisting only of characters ( and ), where each opening bracket
has a matching closing bracket (and each opening bracket must be to the left of its corresponding closing bracket).

Note 2: The following program code:
print(is_correct_bracket('())(()())'))
print(is_correct_bracket(')(())('))

should output:
True
False
"""

# function declaration
def is_correct_bracket(text):
    flag = False
    while '()' in text:
        text = text.replace("()", "")
    if text == "":
        flag = True
    return flag

# read the data
txt = input()

# call the function
print(is_correct_bracket(txt))
