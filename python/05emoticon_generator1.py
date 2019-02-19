# emoticon_generator.py
import random
eye_list = [':', ';', '=', '8', 'B']
nose_list = ['-', ' ', '+', '\'']
mouth_list = [')', '\\', '|', '}', '>']
for count in range(0, 5):
    emot_out = ''
    eye = random.choice(eye_list)
    nose = random.choice(nose_list)
    mouth = random.choice(mouth_list)
    emot_out = eye + nose + mouth + '\n'
    print(emot_out)
