'''
Number guessing game, just run program, and you got instructions
P.S. the program should be able to import random
'''

from random import *

# game algorithm
def guessing_game(x, y):
    phrases_too_much = ['Oh, too much! Try again', 'This will be too much!', "Wow, that's too much!",
                          'Much!', 'Take it lower', 'Too much!', 'Need a smaller number!']
    phrases_too_little = ['Oh, too little! Try again', "It won't be enough!", "Eh, that's too little!",
                           'Take it higher', 'Not enough!', 'We need a larger number!']
    phrases_almost = ['Almost got it right!', 'Hot, but not very', 'Already close', "You're close",
                          "You're already close", "Come on, almost", 'Hot!']
    phrases_guessed = ['Congratulations! You guessed my number :)', 'Well done! You guessed right :)',
                       'Hurray, you guessed right! :)']
    phrases_too_soon = ['Wow, so fast!', "You're a wizard! You guessed my number", 'Tell me honestly, were you spying?',
                        'You have excellent intuition!', "Even I couldn't guess so quickly!"]
    if x > y:
        x, y = y, x
        num_0 = randint(x, y)
        print('I guessed the number from', x, 'до', y, 'Try to guess!')
    else:
        num_0 = randint(x, y)
        print('I guessed the number from', x, 'до', y, 'Try to guess!')
    count = 0
    while True:
        num_1 = int(input())
        count += 1
        if num_1 == num_0:
            if count == 1:
                print('Tell me honestly, did you spy?')
                if input('Do you want to play again? Enter "y" or "n"').lower() in ['yes', 'y']:
                    start()
                else:
                    print('Come back when you want to play again :)')
                    break
            elif 1 <= count <= 5:
                print(choice(phrases_too_soon))
                if input('Do you want to play again? Enter "y" or "n"').lower() in ['yes', 'y']:
                    start()
                else:
                    print('Come back when you want to play again :)')
                    break
            else:
                print(choice(phrases_guessed))
                if input('Do you want to play again? Enter "y" or "n"').lower() in ['yes', 'y']:
                    start()
                else:
                    print('Come back when you want to play again :)')
                    break
        elif num_1 > num_0:
            if abs(num_1 - num_0) < 5:
                print(choice(phrases_too_much), choice(phrases_almost), sep='\n')
            else:
                print(choice(phrases_too_much))
        elif num_1 < num_0:
            if abs(num_1 - num_0) < 5:
                print(choice(phrases_too_little), choice(phrases_almost),  sep='\n')
            else:
                print(choice(phrases_too_little))

# describe the rules
def game_rules():
    print('Great! Let me introduce you to the rules of the game.')
    print('I will guess a number, and you will guess it.')
    print('You choose the range of numbers yourself.')
    print('For example, if you specify a range of numbers from 0 to 100, I will not be able to guess the number "101" :)')
    print("I'll ask you to enter the range limits. Borders must not coincide! We can't play like that.")
    input('Now write something so I can be sure you understand the rules of the game :)')

# checking for correctness
def is_valid_x(x):
    if x.isdigit() is False:
        print('You entered not a number :(')
        print('Well, okay, enter new numbers.')
        start()

def is_valid_xy(x, y):
    while x == y:
        print("You entered the same numbers. I told you we can't play like this :(")
        print('Well, okay, enter new numbers.')
        start()
    if y.isdigit() is False:
        print("I'm confused :( It's not a number")
        print("Let's do it again :)")
        start()
    else:
        return True

# launching the game
def start():
    x = input('Enter the first range limit: ')
    is_valid_x(x)
    y = input('Enter the second range limit: ')
    if is_valid_xy(x, y) is True:
        x, y = int(x), int(y)
        guessing_game(x, y)

# invitation to the game
if input('Greetings! Would you like to play a game? Enter "yes" or "no" ').lower() in ['yes', 'y']:
    game_rules()
    start()
else:
    if input("It won't take much time or effort. If you still think about it, enter “yes” :) ").lower() in ['yes', 'y']:
        game_rules()
        start()
    else:
        print('Come when you want to play :)')