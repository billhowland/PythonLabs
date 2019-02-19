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

    q = (total // 25)
    print ((str(round(q))) + (' Quarters'))
    remaind = total - (q * 25)
    d = (remaind // 10)
    print ((str(round(d))) + (' Dimes'))
    remainn = remaind - (d * 10)
    n = (remainn // 5)
    print ((str(round(n))) + (' Nickles'))
    remainp = remainn - (n * 5)
    p = (remainp // 1)
    print ((str(round(p))) + (' Pennies'))


    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
