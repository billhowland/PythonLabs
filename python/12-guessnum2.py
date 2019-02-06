# 12-guessnum1.py
# Version 2:

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
    while guesses < 10:
        guess = int(input('Guess the number: '))
        guesses += 1
        if guess != secret_num:
            print('Try again!')
        else:
            print (('Correct! It took you') + ' ' + (str(guesses)) + ' ' + ('tries.'))

#----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
