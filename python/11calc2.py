# 11-calc1.py
# Version 2:


while True:

    op = input('What is the operation? ')
    if op == 'done':
        print('Goodbye!')
        break
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
