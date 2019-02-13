# 99-template.py
# Version X:

# define functions here-------------------------------------------


def check_palindrome(word):
    pass


# def func():

def main():
    word = input('enter a word: ')
    check_palindrome(word)

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
