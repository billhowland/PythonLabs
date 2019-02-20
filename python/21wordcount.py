# 21wordcount.py
# Version 1:
import requests
import string
# define functions here-------------------------------------------


def get_book():
    res = requests.get('http://www.gutenberg.org/ebooks/50742.txt.utf-8')
    if res:
        book_in = res.text
    return book_in.lower().strip().translate(string.punctuation)


# def func():

def main():
    book = get_book()
    print(book)


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
