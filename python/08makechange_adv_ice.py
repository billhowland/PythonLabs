# makechange_ice.py

print('This program calculates coins for making change')
run = 1
while(run):
    while True:
        total = input('Enter the amount > ').strip().strip('$')
        try:
            total = (float(total)) * 100
            if total < 0:
                raise ValueError
            break
        except ValueError:
            print('Enter positive numbers only, dude.')

    denom = {
        'hundreds': 10000,
        'fifties': 5000,
        'twenties': 2000,
        'tens': 1000,
        'fives': 500,
        'ones': 100,
        'quarters': 25,
        'dimes': 10,
        'nickles': 5,
        'pennies': 1
    }

    change = ['Your change is: ']

    for d in denom:
        d_change = total // denom[d]
        total %= denom[d]
        change.append(f'{round(d_change)} {d}')

    print(', '.join(change))

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
