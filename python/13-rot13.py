# averages.py
# Version 1:

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']
def encode (ine): #(rot) chars right
    lindex = (alph.index(ine)) + rot
    if lindex > 25:
        lindex -= 26
    return alph[lindex]

def decode (ind): #(rot) chars left
    lindex = (alph.index(ind)) - rot
    if lindex > 25:
        lindex -= 26
    return alph[lindex]

#----------------------------------------------------------------------

run = 1
while run:

    #----------------------------------------------------------------------------------------------------------------------------
        
    dir = input('(e)ncode or (d)ecode? > ').strip().lower()
    rot = int(input('Enter your rotation factor > '))
    if dir == ('e'):
        prac = input('Input message to encode > ')
        listb = []
        for ine in prac:
            lista = (encode (ine))
            listb += lista
        print (''.join(listb))
    elif dir == ('d'):
        prac = input('Input message to decode > ')
        listb = []
        for ine in prac:
            lista = (decode (ine))
            listb += lista
        print (''.join(listb))

    #----------------------------------------------------------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
