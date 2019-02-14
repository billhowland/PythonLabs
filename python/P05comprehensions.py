# P05-comprehensions.py
# Version X:

# define functions here--------------------------------------------------------


def add(a, b):
    return a + b

# Write a comprehension to generate the first 10 powers of two:


def pwrs(n):
    return [2**i for i in range(0, n)]


def evns(n):
    return [i * 2 for i in range(1, 11)]


def evns_f(n):
    return [i for i in range(n) if not i % 2]
# def x ():


def main():
    print(add(5, 2))
    print(add(8, 1))
    print(pwrs(10))
    print(evns(10))
    print(evns_f(20))

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    run = 1
    while run:

        # ---------------------------------------------------------------------

        main()

# -----------------------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
