# 20ccv.py - Credit Card Validation
# Version 1:

iters = ['first', 'second', 'third']
valid_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               '10': 10, 'j': 10, 'k': 10, 'q': 10, 'a': 1}


# define functions here-------------------------------------------


def validate(ccv_in):
    ccv = (list(ccv_in))
    return (ccv)


def main():
    print(validate('1234'))

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
