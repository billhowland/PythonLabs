# 12-guessnum3.py
# Version 3:

import random
guesses = 0
#define functions here-------------------------------------------------------------------------------------------------------

#define()

#----------------------------------------------------------------------------------------------------------------------------

run = 1
while run:

#---|TAB---------------------------------------------------------------------------------------------------------------------

    secret_num = random.randint(1,10)
    #print (secret_num)
    while True:
        guess = int(input('Guess the number: '))
        guesses += 1

        if guess < secret_num:
            print('Too low....')
        elif guess > secret_num:
            print('Too high....')
        elif guess == secret_num:
            print (('Correct! It took you') + ' ' + (str(guesses)) + ' ' + ('tries.'))
            break

    guesses = 0
#----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
