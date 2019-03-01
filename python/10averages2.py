# averages.py
# Version 1:


run = 1
while run:

    # ---|TAB------------------------------------------------------------------

    calc = 1
    nums = []
    tot_l = 0
    while calc == 1:

        avg_in = input('Enter a number, or (d)one: ')
        if avg_in == 'd':
            calc = 0

        else:
            nums.append(avg_in)

    for num in nums:
        tot_l += int(num)
    print(tot_l / len(nums))


# -----------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
