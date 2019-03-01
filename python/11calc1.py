# 11-calc1.py
# Version 1:


run = 1
while run:

    # ---|TAB------------------------------------------------------------------

    op = input('What is the operation? ')
    numa = float(input('what is the first number? '))
    numb = float(input('what is the second number? '))

    print((((str(numa))) + ' ' + (op) + ' ' + (str((numb))) + ' = '), end='')
    if op == '+':
        print(numa + numb)
    elif op == '-':
        print(numa - numb)
    elif op == '/':
        if numb != 0:
            print(numa / numb)
        else:
            print("I don't divide by 0, idiot!")
    elif op == '*':
        print(numa * numb)
    else:
        print("bogus operator, retry")


# -----------------------------------------------------------------------------

    ask = input('Quit? Y/N > ').strip().lower()
    if ask == 'y':
        run = 0
