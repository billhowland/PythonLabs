// # unitconverter.py
// # Version 4:
//
// run = 1
//
// while run:
//
//     def conv(to_units):
//         conv_facts = {'feet' : .3048, 'miles' : 1609.34, 'meters' : 1, 'kilometers' : 1000, 'yards' : .9144, 'inches': .0254,
//         'f' : .3048, 'mi' : 1609.34, 'm' : 1, 'km' : 1000, 'y' : .9144, 'i' : .0254, 'in' : .0254}
//         conva_fact = conv_facts.get(unit_in)
//         convb_fact = conv_facts.get(conv_to)
//         return ((to_units * conva_fact) / convb_fact)
//
//
//     to_conv = int(input('Please enter the distance > '))
//     unit_in = input('Please enter the original unit of measure > ').lower().strip()
//     conv_to = input('What output units would you like? > ')
//
//     print ((str(to_conv)) + ' ' + (str(unit_in)) + ' = ' + (str(conv(to_conv))) + ' ' + (str(conv_to)))
//
//     ask = input('Quit? Y/N > ').strip().lower()
//     if ask == 'y':
//         run = 0

// unitconverter.js


let conv = (to_units, unit_in, conv_to) => {
    conv_facts = {'feet' : .3048, 'miles' : 1609.34, 'meters' : 1, 'kilometers' : 1000, 'yards' : .9144, 'inches': .0254,
    'f' : .3048, 'mi' : 1609.34, 'm' : 1, 'km' : 1000, 'y' : .9144, 'i' : .0254, 'in' : .0254}
    conva_fact = conv_facts[unit_in]
    convb_fact = conv_facts[conv_to]
    return ((to_units * conva_fact) / convb_fact)
  }
to_conv = prompt('Please enter the distance:');
unit_in = prompt('Please enter the original unit of measure:');
conv_to = prompt('What output units would you like?:');
alert ((to_conv) + ' ' + (unit_in) + ' = ' + (conv(to_conv, unit_in, conv_to)) + ' ' + (conv_to))
