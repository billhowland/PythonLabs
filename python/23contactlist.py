# 23contactlist.py
# Version 1:

# define functions here-------------------------------------------

# def func():

# def func():


def main():
    contact = {}
    keys = ''
    vals = ''
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
    # print(lines)
    for i, line in enumerate(lines):
        if i == 0:
            keys = line.split(",")
            # print(keys)
        else:
            vals = line.split(",")
            # print(vals)
            for k, key in enumerate(keys):
                print(k)
                print(key)
                if vals[k] != (''):
                    contact.update({str(key): str(vals[k])})
                    print(contact)


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
