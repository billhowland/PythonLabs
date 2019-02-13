# rock_paper_scissors

import random

def results(pc, user):
    defeats = {
        'r': 's',
        'p': 'r',
        's': 'p'
    }

    if pc == user:
        return 'Tie'
    elif defeats[pc] == user:
        return 'I Win!'
    else:
        return "You Win!"

play = 'y'
while play == 'y':

    rps_list = ['r', 'p', 's']
    while True:
        user = input('Choose Rock (r), Paper (p), or Scissors (s) > ').strip().lower()#.startswith()
        if user not in rps_list:
            print('Entry error!')
            continue
        break

    pc = random.choice(rps_list)
    print(pc)
    print(results(pc, user))

    play = input('Play again? y/n > ')
    if play == 'n':
        print("Seeya, Chicken!!!")
