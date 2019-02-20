# 20ccv.py - Credit Card Validation
# Version 1:


# define functions here-------------------------------------------


def validate(ccv_in):
    ccv = [i for i in (ccv_in) if i.isdigit()]
    check_dig = int(ccv.pop())
    ccv.reverse()
    ccv = sum(int(c) for c in ''.join(str(int(x)*(2-i % 2)) for i, x in
                                      enumerate(ccv)))
    return check_dig == (ccv % 10)


def main():
    while True:
        vcc = input('Enter the card number: > ')
        if vcc.isdigit():
            print(validate(vcc))
            break
        else:
            print('Invalid Entry')

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
