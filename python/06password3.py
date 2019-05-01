# 06-password3.py

import random
seed_lower = ('correcthorsebatterystaple')
seed_upper = ('GETTHEHELLOUTTAHERETHEPLANETSONFIRE')
seed_spec = ('!@#$%^&*?')

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
