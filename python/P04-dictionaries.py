# averages.py
# Version 1:

run = 1
while run:

    #----------------------------------------------------------------------------------------------------------------------------
    def combined(a, b):
        price_list = {}
        for i in range (len(a)):
            print(i, a[i], b[i])
            price_list [a[i]] = b[i]
        return price_list

    fruits = ['applejacks', 'booberry', 'peanut butter crunch']
    prices = [4.49, 3.89, 5.09]
    print(combined(fruits, prices))


    #----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
