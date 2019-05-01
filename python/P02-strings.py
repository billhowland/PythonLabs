# Practice 02-Strings.py

# example:


def add(a, b):
    return a + b
# print(add(5, 2))
# print(add(8, 1))

# Problem 1:


def double_letters(x):
    double = ''
    for char in x:
        double += char * 2
    return double


# return ''.join([char*2 for char in text])

print(double_letters('hello'))


#
