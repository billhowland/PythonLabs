# SockSorter.py
# Version 2:

import random
allsocks = []
socktypes = ['ankle', 'crew', 'calf', 'thigh']
colors = ['black', 'white', 'blue']
sorter = {}

# define functions here-------------------------------------------------------------------------------------------------------

# def

# ---------------------------------------------------------------------------------------------------------------------------

run = 1
while run:

    # ---|TAB---------------------------------------------------------------------------------------------------------------------

    for i in range(100):
        sock = random.choice(socktypes)
        color = random.choice(colors)
        allsocks.append((sock, color))

        sorter[(sock, color)] = sorter.get((sock, color), 0) + 1

    print(allsocks)
    print(sorter)

    for sock in sorter:
        print(f'{sock} has {sorter[sock]%2} loner(s)')

    # ----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
