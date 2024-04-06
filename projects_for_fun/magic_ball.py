'''
Just a magic ball that returns random funny answers to any question
'''

import random as rnd
answers = ["Certainly", "As I see it, yes", "It is not clear yet, try again",
           "Don't even think about it",
           "It is certain", "Most likely", "Ask again later", "My answer is no",
           "No doubts", "Good prospects", "Better not to tell",
           "According to my data - no",
           "You can count on it", "Yes", "Concentrate and ask again",
           "Very doubtful"]

print('Hello World, I am the magic ball, and I know the answer to any of your questions.')
name = input('Name yourself: ')
print(f'Greetings to you, oh {name}!')
again = 'y'
while again.lower() == 'y':
    print('You can ask your question:')
    _ = input()
    print(f'I can answer that: {rnd.choice(answers)}...')
    again = input(f'Do you have any more questions, oh {name}? (y = yes, n = no): ')

print(f'Come back if you have any questions, dear {name}!')

