'''
Write a program that reads a delimiter line and three lines, line end of them, and then outputs
the specified lines through the delimiter which ended specific line
'''
delimiter = input() #as example "+"
ender = input() #as example "="
print(input(), input(), input(), sep=delimiter, end=ender)  #23, 2, df -> 23+2+df=