# 25atm.py
# Version 1:


class Acct:
    def __init__(self, name, balance):
        self.name = name
        self.bal = balance

    def check_bal(self):
        print(f'${self.bal}')

    def acct_dep(self, amount):
        self.bal += amount

    def check_over(self, amount):
        return ((self.bal - amount) < 0)

    def acct_with(self, amount):
        if not self.check_over(amount):
            self.bal -= amount
        else:
            print(f'{self.name} has insufficient funds')


def main():
    test = Acct('Bill', 1000)
    test.check_bal()

    test.acct_with(500)
    test.check_bal()

    test.acct_dep(2000)
    test.check_bal()
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
