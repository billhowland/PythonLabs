# 23contactlist.py
# Version 1:

# define functions here-------------------------------------------


# def func():


def main():
    contact_list = {}
    keys = ''
    vals = ''
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
    for i, line in enumerate(lines):
        contact = {}
        if i == 0:
            keys = line.split(",")
        else:
            vals = line.split(",")
            if line.strip():
                for k, key in enumerate(keys):
                    contact.update({str(key): str(vals[k])})
                contact_list[contact['name']] = contact
    print(contact_list)

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
