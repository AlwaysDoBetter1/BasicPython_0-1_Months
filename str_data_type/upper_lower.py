"""
Find words that have uppercase and lowercase using methods upper and lower
"""

string = input()  #line for checking
lower1, upper1 = 0, 0
for i in range(len(string)):
    if string[i].upper() != string[i]:  # find lowercase words
        lower1 +=1
    elif string[i].lower() != string[i]: # find uppercase words
        upper1 += 1

print(f"lower: {lower1}, upper: {upper1}")