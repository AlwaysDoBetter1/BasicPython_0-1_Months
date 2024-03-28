"""
Write a function print_fio(name, surname, patronymic) that takes three parameters:

name – person’s name;
surname – person’s surname;
patronymic – a person’s patronymic;

and then prints the person’s full name.

"""

# function declaration
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

# read the data
name, surname, patronymic = input(), input(), input()
'''
Alexander
Pushkin
Sergeevich

for fast checking
'''
# call the function
print_fio(name, surname, patronymic)
