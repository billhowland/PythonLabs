# 25atm2.py
# Version 2:

# --------------------------------------------------------------------------


class Acct:
    def __init__(self, name, balance):
        self.name = name
        self.bal = balance
        self.trans_list = []

    def check_bal(self):
        print(f'Account balance is: ${self.bal}')

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

# --------------------------------------------------------------------------


def main():
    loop = True
    valid_inputs = [
        'd', 'deposit',
        'w', 'withdraw',
        'c', 'check',
        'h', 'history',
        'n', 'new account',
        'x', 'exit', 'quit',
        ]
    commands = """
        Commands:
        (d)eposit
        (w)ithdraw
        (c)heck balance
        (h)istory
        (n)ew account
        e(x)it
    """

    print('Welcome to First Interstellar Bank')

    acct = Acct(input('Enter account name: ').strip().lower(), 0)

    print(commands)

    while loop:
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

        elif cmd.startswith('d'):  # deposit
            try:
                acct.acct_dep(int(input('Deposit amount: ')))
                continue
            except ValueError:
                print('Invalid input.')

        elif cmd.startswith('w'):  # Withdraw
            acct.acct_with(int(input('Withdrawal amount: ')))

        elif cmd.startswith('c'):  # check balance
            acct.check_bal()

        elif cmd.startswith('h'):  # transacton history
            acct.print_trans()

        elif cmd.startswith('n'):  # transacton history
            loop = False

# ----------------------------------------------------------------


if __name__ == '__main__':

    run = 1
    while run:

        # --------------------------------------------------------

        main()
