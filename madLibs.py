# Mad Libs

#<name> <verb> through the forest, hoping to escape the <adjective><noun>.

import random

namesList = ['Weird Al Yankovi', 'The Teenage Mutant Ninja Turtles', 'supergirl',\
             'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
             'The Beatles', 'Powerpuff Girl', 'The Pillsbury Doughboy',\
             'Sam-I-Am']

verbList = ['run', 'crash', 'fly', 'burp', 'scream', 'flash']

adjectiveList = ['big', 'fat', 'rusty', 'Dark', 'round']

nounList = ['ghost', 'crow', 'witch', 'house', 'frisbee']

while True:
    
    name = random.choice(namesList)
    verb = random.choice(verbList)
    adjective = random.choice(adjectiveList)
    noun = random.choice(nounList)

    sentence = name + ' ' + verb + ' through the forest, hoping to escape the '\
               + adjective + ' ' + noun + '.'
    print()
    print(sentence)
    print()

    # ask if the user wants to quit
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue: ')
    if answer == 'q':
        break

print('Bye')
