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
    test = Acct('Bill', 1000)
    test.check_bal()
    test.acct_with(500)
    test.check_bal()
    test.acct_dep(2000)
    test.check_bal()
    test.print_trans()
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
