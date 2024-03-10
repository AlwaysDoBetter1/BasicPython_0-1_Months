'''
We will consider an email address to be correct if it contains a dog symbol (@) and a dot (.).
Write a program that checks the validity of an email address.

Input format
The program receives one line as input – an email address.

Output format
The program should output the line “YES” if the email address is correct and “NO” otherwise.

Note. For real email addresses, the presence of the @ and . symbols is not enough, but their absence
is guaranteed to result in an incorrect email.
'''
a = input() #email
print("YES" if "@" in a and "." in a else "NO") #correct or no