# 06-password2.py

import random
seed = ('correcthorsebatterystaple')
a = 0
password = ''

print('The Automagical Random Password Generator')
n = int(input("How many characters for your new password? > "))


while a < n:
    seed_var = random.choice(seed)
    password += seed_var
    a += 1
    continue
print(password)
