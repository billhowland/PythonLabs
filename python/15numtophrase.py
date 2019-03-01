# 15numtophrase.py
# Version 1:

diction_one = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
diction_two = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
               14: 'fourteen', 15: 'fifteen'}
diction_thr = {0: '', 1: 'teen', 2: 'twenty', 3: 'thirty', 4: 'forty',
               5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

# define functions here---------------------------------------------------


def verbose(num):
    huns_dig = (num // 100)
    tens_dig = (num // 10 % 10)
    ones_dig = (num % 10)
    if tens_dig > 0 and ones_dig == 0:
        return (diction_thr[tens_dig])
    if tens_dig == 0:
        return (diction_one[ones_dig])
    return (diction_thr[tens_dig] + '-' + diction_one[ones_dig])


def verbodds(num):
    return (diction_two[num])


def verbteens(num):
    huns_dig = (num // 100)
    tens_dig = (num // 10 % 10)
    ones_dig = (num % 10)
    # return (str(huns_dig) + str(tens_dig) + str(ones_dig))
    return (diction_one[ones_dig] + diction_thr[tens_dig])


def main():
    while True:
        try:
            inpnum = int(input('Enter the number: '))
            break
        except ValueError:
            print('Numbers, f00L!')

    if inpnum in range(10, 16):
        print(verbodds(inpnum))
    elif inpnum in range(16, 20):
        print(verbteens(inpnum))
    else:
        print(verbose(inpnum))


# ------------------------------------------------------------------------
if __name__ == '__main__':

    run = 1
    while run:

        # ----------------------------------------------------------------

        main()
# ------------------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0

# ------------------------------------------------------------------------
