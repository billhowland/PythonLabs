# 12-guessnum2.py
# Version 2:

import random
guesses = 0

run = 1
while run:

    secret_num = random.randint(1, 10)
    # print (secret_num)
    while True:
        guess = int(input('Guess the number: '))
        guesses += 1
        if guess != secret_num:
            print('Try again!')

        else:
            print(('Correct! It took you') + ' ' + (str(guesses)) + ' ' + ('tries.'))
            break

    guesses = 0

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
