# magic 8 ball1.py UNFINISHED
import random

a = 1
while a == 1:

    print("Welcome to Magic 8-Ball. I help with life's toughest questions.")
    pred_list = ["Absolutely", "Negatory, Ghost Rider",
                 "In a universe it isn't prohibited in, it's guaranteed to occur eventually",
                 "You'll have better luck at the lottery, Oh dreamy one!"]
    quest = input("What is your most intimate curiosity? > ")
    print(f"The Demons say: {random.choice(pred_list)}")
    rept = input("Have another query? > ").strip().lower()
    if rept in ['no', 'n']:
        a = 0
