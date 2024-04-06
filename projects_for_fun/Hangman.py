"""
That program allows you to play classic hangman
"""

import random
import time

print('Let\'s play Hangman!')

word_list = [
    ['Odessa', 'Kyiv', 'London', 'Amsterdam', 'Moscow'],
    ['cat', 'dog', 'platypus', 'hedgehog'],
    ['potato', 'dumplings', 'salad', 'omelette', 'sandwich']
]

def get_word():
    print()
    print("Choose a category: ")
    options = int(input("Cities - 1; Animals - 2; Food - 3: "))
    x = options - 1
    return random.choice(word_list[x]).lower()

def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
        ''',
        '''                   
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
        ''',
        '''                   
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
        ''',
        '''                   
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
        ''',
        '''                   
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
        ''',
        '''                   
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
        ''',
        '''                   
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = ['_ '] * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries), 'Tries left:', tries)
    print(*word_completion)

    while True:
        if tries == 0:
            print('\nYou lost! The word was:', word)
            break

        if word_completion.count('_ ') == 0:
            print('\nCongratulations, you guessed the word! You win!')
            break

        print()
        l = input("Guess a letter or the whole word: ").lower()
        if len(l) == 1:
            if l in guessed_letters:
                print('\nYou already guessed that letter!')
                print(display_hangman(tries), 'Tries left:', tries)
                print(*word_completion)

            elif l in word:
                print('\nCorrect!')
                guessed_letters.append(l)
                for i in range(len(word)):
                    if word[i] == l:
                        word_completion[i] = l
                print(display_hangman(tries), 'Tries left:', tries)
                print(*word_completion)

            elif l not in word:
                guessed_letters.append(l)
                print('\nNo such letter!')
                tries -= 1
                print(display_hangman(tries), 'Tries left:', tries)
                print(*word_completion)

        elif len(l) > 1:
            if l in guessed_words:
                print('\nYou already guessed that word!')
                print(display_hangman(tries), 'Tries left:', tries)
                print(*word_completion)

            elif l == word:
                print('\nCongratulations, you guessed the word! You win!')
                break

            elif l != word:
                guessed_words.append(l)
                print('\nIncorrect!')
                tries -= 1
                print(display_hangman(tries), 'Tries left:', tries)
                print(*word_completion)


while True:
    x = get_word()
    play(x)
    q = input('Play again? (y = yes, n = no): ')
    if q == 'y':
        continue
    else:
        print('Goodbye!')
        time.sleep(2)
        break
