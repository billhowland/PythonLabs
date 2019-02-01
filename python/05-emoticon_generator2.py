# emoticon_generator.py

eye_list = [':', ';', '=', '8', 'B']
nose_list = ['-', ' ', '+', '\'']
mouth_list  = [')', '\\', '|', '}', '>']
eye_ch = input(f"Choose eyes from {eye_list} > ")
nose_ch = input(f"Choose nose from {nose_list} > ")
mouth_ch = input(f"Choose mouth from {mouth_list} > ")
emot_out = ''
emot_out = eye_ch + nose_ch + mouth_ch + '\n'
print (emot_out)
