# 23contactlist.py
# Version 2:

# define functions here-------------------------------------------

# def func():

# def func():


def main():
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
    print(lines)

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
