# 25atm.py
# Version 1:


class Acct:
    def __init__(self, name, balance):
        self.name = name
        self.bal = balance
        self.trans_list = []

    def check_bal(self):
        print(f'${self.bal}')

    def acct_dep(self, amount):
        self.bal += amount
        self.trans_list.append(f'{self.name} deposited ${amount}')

    def check_over(self, amount):
        return ((self.bal - amount) < 0)

    def acct_with(self, amount):
        if not self.check_over(amount):
            self.bal -= amount
            self.trans_list.append(f'{self.name} withdrew ${amount}')
        else:
            print(f'{self.name} has insufficient funds')

    def print_trans(self):
        print(self.trans_list)


def main():
    # test = Acct('Bill', 1000)
    # test.check_bal()
    # test.acct_with(500)
    # test.check_bal()
    # test.acct_dep(2000)
    # test.check_bal()
    # test.print_trans()
    loop = True
    valid_inputs = [
        'd', 'deposit',
        'w', 'withdraw',
        'c', 'check',
        'h', 'history',
        'x', 'exit', 'quit',
        'h', 'help'
    ]
    commands = """
        Commands:
        (d)eposit
        (w)ithdraw
        (c)heck balance
        (h)istory
        e(x)it
        (h)elp
    """

    print('Welcome to First Interstellar Bank')
    print(commands)

    while loop:
        print('-'*60)
        while True:
            cmd = input('> ').strip().lower()
        if cmd in valid_inputs:
            break
        print('Invalid input.')
        print(commands)

        if cmd in ['x', 'exit', 'quit']:
            # save(contacts, 'contacts_out.csv')
            loop = False
            print('Goodbye!')

        elif cmd in ['h', 'help']:
            print(commands)

        elif cmd.startswith('c'):
            contact = {}
            for prop in props:
                contact[prop] = input(f'{prop}: ')
            print(create(contacts, contact))

        elif cmd.startswith('r'):
            name = input('name: ')
            contact = read(contacts, name)
            print_contact(contact)

        elif cmd.startswith('u'):
            name = input('name: ')
            contact = {}
            for prop in props:
                val = input(f'{prop}: ')
                if val:
                    contact[prop] = val
            print(update(contacts, name, contact))

        elif cmd.startswith('d'):
            name = input('name: ')
print(delete(contacts, name))


# what would you like to do (deposit, withdraw, check balance, history)?
# deposit
# how much would you like to deposit?
# $5
# what would you like to do (deposit, withdraw, check balance, history)?
# check balance
# balance: $5
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
