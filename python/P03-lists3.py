# Practice 03-Lists3.py

# Problem 3:

import random


def random_element(a):
    if len(a) == 0:
        return 'empty list'
    index = random.randint(0, len(a)-1)
    return a[index]


def eveneven(numlist):
    # nums = 0
    # for item in numlist:
    #    if item % 2 == 0:
    #        nums += 1
    # return nums % 2 == 0

    return len([num for num in numlist if num % 2 == 0]) % 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(eveneven(numbers))
numbers2 = [2, 3, 4, 5, 6, 7]
print(eveneven(numbers2))

# fruits = ['applejacks', 'booberry', 'captain crunch']
# print(random_element(fruits))
