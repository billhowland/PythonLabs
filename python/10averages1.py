# averages.py
# Version 1:

run = 1
while run:

#define functions here-------------------------------------------------------------------------------------------------------

#define()

#---|TAB---------------------------------------------------------------------------------------------------------------------

    nums = [5, 0, 8, 3, 4, 1, 6]
    tot_l = 0

    # loop over the elements
    for num in nums:
        tot_l += int(num)
    print(tot_l / len(nums))

    # loop over the indices
    # for i in range(len(nums)):
        # print(nums[i])

#----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
