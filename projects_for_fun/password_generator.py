import random as rnd

def generate_password(length, characters):
    '''
    Generates a password of specified length using given characters.

    :param length: int, length of the password
    :param characters: str, characters to use for generating the password
    :return: str, generated password
    '''
    password = ''
    for _ in range(length):
        password += rnd.choice(characters)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
characters = ''

count_pass = int(input('How many passwords to generate? '))
length_pass = int(input('Password length: '))

if input('Press 1 to allow lowercase letters: ') == '1':
    characters += lowercase_letters

if input('Press 1 to allow uppercase letters: ') == '1':
    characters += uppercase_letters

if input('Press 1 to allow digits: ') == '1':
    characters += digits

if input('Press 1 to allow punctuation: ') == '1':
    characters += punctuation

if input('Press 1 to exclude ambiguous characters "il1Lo0O": ') != '1':
    for char in 'il1Lo0O':
        characters = characters.replace(char, '')

for _ in range(count_pass):
    print(generate_password(length_pass, characters))