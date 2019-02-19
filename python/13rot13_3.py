# averages.py
# Version 1:

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']
def encode (ine, rot): #(rot) chars right
    lindex = (alph.index(ine)) + rot % 26
    if lindex > 25:
        lindex -= 26
    return alph[lindex]

def decode (ind, rot): #(rot) chars left
    lindex = (alph.index(ind)) - rot % 26
    if lindex > 25:
        lindex -= 26
    return alph[lindex]

def main ():
    while True:
        dir = input('(e)ncode or (d)ecode? > ').strip().lower()
        if dir in ['e', 'd']:
            break
    while True:
        try:
            rot = int(input('Enter your rotation factor > '))
            break
        except ValueError:
            print('Numbers Only!')

    if dir == ('e'):
        prac = input('Input message to encode > ')
        listb = []
        for ine in prac:
            if ine not in alph:
                lista = ine
            else:
                lista = (encode (ine, rot))
            listb += lista
        print (('Here is your encoded message: ') + (''.join(listb)))
    elif dir == ('d'):
        prac = input('Input message to decode > ')
        listb = []
        for ine in prac:
            if ine not in alph:
                lista = ine
            else:
                lista = (decode (ine, rot))
            listb += lista
        print (('Here is your decoded message: ') + (''.join(listb)))

#----------------------------------------------------------------------

if __name__ == '__main__':
    run = 1
    while run:

#----------------------------------------------------------------------------------------------------------------------------

        main()

#----------------------------------------------------------------------------------------------------------------------------

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
