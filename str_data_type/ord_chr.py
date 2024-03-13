"""
Decode the text using the Caesar cipher, this is a replacement of words shifted by "n" to the right

Input format The first line gives the number n (1≤ n≤ 25) – shift, the second line gives the encoded message in the
form of a string with lowercase Latin letters.

Output format
The program should output one line - the decoded message. Note that you need to decode the message, not encode it.
"""

n = int(input())  # steps of shifting
for i in input():  # line for decode
    # if during a shift we reach the beginning of the alphabet, we need to continue the shift from the end of the
    # alphabet
    if ord(i) - n >= 97:  # if shift don't reach the beginning of the alphabet
        print(chr(ord(i) - n), end="")
    else:  # if shift reach the beginning of the alphabet
        print(chr(ord(i) - n + 26), end="")

# example:
# 1
# bwfusvfupdbftbs
