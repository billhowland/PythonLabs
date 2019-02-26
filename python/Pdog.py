# Pdog.py
# Version X:

# define functions here-------------------------------------------
# this is another example of a class


class Dog:
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age

    def bark(self):
        print(f'my name is {self.name}, I am a {self.size} dog that is {self.age} years old')


# def func():

# def func():


def main():
    dog1 = Dog('Fido', 'big', 3)
    dog1.bark()

    dog1.age = 8
    dog1.bark()
# ----------------------------------------------------------------


if __name__ == '__main__':

    run = 1
    while run:

        # --------------------------------------------------------

        main()

# ----------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
