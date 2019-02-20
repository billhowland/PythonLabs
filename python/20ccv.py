# 20ccv.py - Credit Card Validation
# Version 1:


# define functions here-------------------------------------------


def validate(ccv_in):
    ccv = [i for i in (ccv_in) if i.isdigit()]
    check_dig = ccv.pop()
    ccv.reverse()
    for i in ccv:


def main():
    print(validate('1234 5678 9234 3456'))

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
