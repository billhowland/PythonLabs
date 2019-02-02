#Practice 03-Lists.py

#Problem 1:

import random
def random_element(a):
    if len(a) == 0:
        return 'empty list'
    index = random.randint(0, len(a)-1)
    return a[index]

fruits = ['applejacks', 'booberry', 'captain crunch']
print(random_element(fruits))
