# makechange2.py
# I made version 2 first by accident!

print('This program calculates coins for making change')
run = 1
while(run):
    total = 100 * (float(input('Enter the amount > ').strip()))
    # print(total)
    q = (total // 25)
    print((str(q)) + (' Quarters'))
    remaind = total - (q * 25)
    # print (remaind)
    d = (remaind // 10)
    print((str(d)) + (' Dimes'))
    remainn = remaind - (d * 10)
    # print (remainn)
    n = (remainn // 5)
    print((str(n)) + (' Nickles'))
    remainp = remainn - (n * 5)
    # print (remainp)
    p = (remainp // 1)
    print((str(p)) + (' Pennies'))

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
