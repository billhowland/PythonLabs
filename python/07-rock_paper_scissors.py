# rock_paper_scissors
import random
play = 'y'
while play == 'y':

    user = input('Choose Rock (r), Paper (p), or Scissors (s) > ')
    rps_list = ['r', 'p', 's']
    x = random.choice(rps_list)
    print('I chose ' + x)
    if user == x:
        result = 'Tie'
    elif user == 'r' and x == 'p' or user == 'p' and x == 's' or user == 's' and x == 'r':
        result = 'I Win!!'
    elif user == 'r' and x == 's' or user == 'p' and x == 'r' or user == 's' and x == 'p':
        result = 'You Win.'
    print (result)
    play = input('Play again? y/n > ')
    if play == 'n':
        print("Seeya, Chicken!!!")
