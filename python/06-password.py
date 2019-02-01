# 06-password.py

import random
seed = ('correcthorsebatterystaple')
n = 8
a = 0
password = ''
while a < n:
     seed_var = random.choice(seed)
     password += seed_var
     a += 1
     continue
print (password)
