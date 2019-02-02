# unitconverter.py
# Version 2:

def conv(to_meters):
    conv = {'feet' : .3048, 'miles' : 1609.34, 'meters' : 1, 'kilometers' : 1000}
    conv_fact = conv.get(unit_in)
    return (to_meters * conv_fact)


unit_in = input('Please enter the original unit of measure > ').lower().strip()
to_conv = int(input('Please enter how many units to convert to meters > '))
print ((str(to_conv)) + ' ' + (str(unit_in)) + ' = ' + (str(conv(to_conv))) + ' meters')
