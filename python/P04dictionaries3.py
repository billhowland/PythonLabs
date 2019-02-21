# P04dictionaries3.py
# Average numbers whose keys start with the same letter. Output a dictionary
# containing those letters as keys and the averages.

# define functions here--------------------------------------------------------


def unify(d):
    unify_out = {}
    for k, v in d.items():
        if k[0] in unify_out:
            out, count = unify_out[k[0]]
            unify_out[k[0]] = (out + v, count + 1)
        else:
            unify_out[k[0]] = (v, 1)

    return {key: rsum/count for (key, (rsum, count)) in unify_out.items()}


# -----------------------------------------------------------------------------


run = 1
while run:

    # --------------------------------------------------------------------------

    d = {'a1': 4, 'a2': 2, 'a3': 3, 'b1': 10, 'b2': 1, 'b3': 1, 'c1': 4,
         'c2': 5, 'c3': 6}

    print(unify(d))

    # -------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
