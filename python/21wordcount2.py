# 21wordcount2.py
# Version 2: Count how often each unique pair of words is used, then print the
# top 10 most common pairs with their counts.
import requests
from string import punctuation
pair_count = {}

# define functions here-------------------------------------------


def count_pairs(book):
    for i in range(len(book)-1):
        worda = book[i]
        wordb = book[i+1]
        pair_count[(worda, wordb)] = pair_count.get((worda, wordb), 0) + 1
    return pair_count


def get_book():
    translator = str.maketrans('', '', punctuation)
    res = requests.get('http://www.gutenberg.org/ebooks/50742.txt.utf-8')
    if res:
        book_in = res.text
    return (book_in.lower().strip().translate(translator)).split()


def top_ten(word_count):
    words = list(word_count.items())  # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])


def main():
    book = get_book()
    word_count = (count_pairs(book))
    print(top_ten(word_count))


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
