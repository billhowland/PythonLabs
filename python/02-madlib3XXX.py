# Madlib2.py - Bill wuz here
# Split, random, repeatable!

import random
a = 1
b = 1

while b == 1:
    madlib_ant = input("Give me an antonym for 'data' >")
    madlib_adj = input("Give me three adjectives separated by ',' >")
    # print (madlib_adj)
    madlib_adj = madlib_adj.split(',')
    madlib_adjr = random.choice(madlib_adj)
    madlib_buzz = input("Give me a science buzzword >")
    madlib_anim = input("Give me a type of animal (plural) >")
    madlib_scia = input("Give me some science thing >")
    madlib_scib = input("Give me another science thing >")
    madlib_sciadj = input("Give me a science adjective >")

    while a == 1:
        story = input("Ready for a story? <y/n> ")
        if story == ('y'):

            print(f"{madlib_ant} Scientist Job Description:")
            print(f"Seeking a {madlib_adjr} engineer, able to work on half-baked projects with a team of {madlib_anim}.")
            print("Key responsibilities:")
            print(f" - Extract patterns from {madlib_ant}")
            print(f" - Optimize {madlib_scia}")
            print(f" - Transform {madlib_scib} into {madlib_sciadj} material.")

        elif story == ('n'):
            a = 0

            repeat = input("Want to do another? <y/n> ")
                if repeat == ('n'):
                    b = 0
