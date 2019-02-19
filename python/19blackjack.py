# 19-blackjack.py
# Version 1:

# (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

iters = ['first', 'second', 'third']
valid_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               '10': 10, 'j': 10, 'k': 10, 'q': 10, 'a': 1}


# define functions here-------------------------------------------


def user_cards():
    cards = []
    cards_val = 0
    for item in iters:
        while True:
            card = input(f"What is the {item} card? > ").strip().lower()
            if card in valid_cards:
                cards.append(card)
                cards_val += int(valid_cards[card])
                break
    return (cards_val)


def advise(total):
    hint = ()
    if total < 17:
        hint = 'Advise you to hit'
    if total >= 17 and total < 21:
        hint = 'Advise you to stay'
    if total == 21:
        hint = 'Blackjack! You win!'
    if total > 21:
        hint = 'Already Busted!'
    return(hint)


def main():
    total = (user_cards())
    print(f"Total is {total}")
    print(advise(total))

    # ----------------------------------------------------------------


if __name__ == '__main__':

    run = 1
    while run:

        # --------------------------------------------------------

        main()

# ----------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
