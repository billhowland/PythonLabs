# 14-pick6-1.py
# Version 1:

import random

#define functions here-------------------------------------------------------------------------------------------------------

def rand(nums):
    randnums = []
    while nums != 0:
        randnums.append(random.randint(1,100))
        nums -= 1
    return randnums
    return []

def ticket_check(win, pick):
    return [i for i, j in zip(num_set, winnum) if i == j]

def main():
    global winnum
    winnum = (rand(6))
    print (winnum)
    # Loop 100,000 times, pick nums, pay, check, add prize, and total
    loop = 1
    cash = 200000
    earns = 0
    while loop < 100000:
        global num_set
        num_set = (rand(6))
        print (num_set)
        cash -= 2 # dock $2
        # print (cash) # remaining
        print ((str(len(ticket_check(num_set, winnum)))) + ' Matches!')
        prizes = {6 : 25000000,  5 : 1000000, 4 : 50000, 3 : 100, 2 : 7, 1 : 4, 0 : 0}
        cash += int(prizes.get(len(ticket_check(num_set, winnum))))
        earns += int(prizes.get(len(ticket_check(num_set, winnum))))
        print (('You have ') + (str(cash)) + ' dollars left.')
        loop += 1


#----------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    run = 1
    while run:

#----------------------------------------------------------------------------------------------------------------------------

        main()

#----------------------------------------------------------------------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
