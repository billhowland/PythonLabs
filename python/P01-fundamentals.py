# practice - fundamentals.py

# function junction:
def add(a, b):
    return a + b

def is_even(a):
    #if a % 2 == 0:
        #return 'True'
    #elif a % 2 == 1: #else woulda worked here
        #return 'False'
    return a % 2 == 0

def opposite(a, b):
    #if a >=0 and b >= 0:
        #return 'False'
    #if a < 0 and b < 0:
        #return 'False'
    #else:
        #return 'True'
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)

def near_100(num):
    if num > 89 or num < 111:
        return 'True'
    else:
        return 'False'

#def max_of_three(a, b, c):


# function compunction:
print (add(5, 2))
print (add(8, 1))

print (is_even(2))
print (is_even(3))

print(opposite(10, -1))
print(opposite(2, 3))
print(opposite(-1, -1))

print (near_100(50))
print (near_100(99))
print (near_100(105))

print (max_of_three(5, 6, 2))
print (max_of_three(-4, 3, 10))
