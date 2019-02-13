# 15numtophrase.py
# Version 1:

# Add Docstrings!

diction_one = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
               4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine'}
diction_two = {10: 'ten', 11: 'eleven', 12: 'twelve',
               13:   'thirteen', 14: 'fourteen', 15: 'fifteen'}
diction_thr = {0: '', 1: 'teen', 2: 'twenty', 3: 'thirty',
               4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty',
               9: 'ninety'}


# define functions here-------------------------------------------

def verbose(num):
    huns_dig = (num // 100)
    tens_dig = (num // 10 % 10)
    tens_odd = (num % 100)
    ones_dig = (num % 10)
    accum = ('')
    if huns_dig != 0:
        accum = (diction_one[huns_dig] + ' hundred and ')
    if tens_dig != 0:
        if tens_odd in range(10, 16):
            accum += (diction_two[tens_odd] + ' ')
            ones_dig = 0
        elif tens_odd % 100 in range(16, 20):
            accum += ((diction_one[ones_dig] + diction_thr[tens_dig]) + ' ')
            ones_dig = 0
        else:
            accum += (diction_thr[tens_dig] + ' ')
    if ones_dig != 0:
        accum += (diction_one[ones_dig])
    return accum


def main():
    while True:
        try:
            inpnum = int(input('Enter the number: '))
            break
        except ValueError:
            print('Numbers, f00L!')

    print(verbose(inpnum))

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

# ----------------------------------------------------------------
