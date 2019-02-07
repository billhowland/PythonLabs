# P04-dictionaries2.py
# Version 2:

#define functions here-------------------------------------------------------------------------------------------------------

def combined(a, b):
    return dict(zip(a, b))

def averaged(menu):
    return ((sum(menu.values())) / (len(menu)))

#----------------------------------------------------------------------------------------------------------------------------

run = 1
while run:

    #----------------------------------------------------------------------------------------------------------------------------

    fruits = ['applejacks', 'booberry', 'peanut butter crunch']
    prices = [4.49, 3.89, 5.09]
    menu = (combined(fruits, prices))
    print (menu)
    av_price = (averaged(menu))
    print (av_price)


    #----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
