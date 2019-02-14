# Practice 03-Lists6&7.py

import time

# Problem 8: Write a function to combine two lists of equal length into one,
# alternating elements.


def combine(alph, nums):
    return sum([list(i) for i in zip(alph, nums)], [])


alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
        '14', '15', '16', '17', '18', '19', '20']
start = time.time_ns()


print(combine(alph, nums))  # , time.time_ns() - start)
