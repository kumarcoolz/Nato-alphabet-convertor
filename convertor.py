while True:
    name = input('Enter a name: ')
    if name.isalpha() == False:
        print('Enter only alphabets')
    else:
        break

name = list(name.upper())

d = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie',
    'D': 'Delta',   'E': 'Echo',     'F': 'Foxtrot',
    'G': 'Golf',    'H': 'Hotel',    'I': 'India',
    'J': 'Juliett', 'K': 'Kilo',     'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',
    'P': 'Papa',    'Q': 'Quebec',   'R': 'Romeo',
    'S': 'Sierra',  'T': 'Tango',    'U': 'Uniform',
    'V': 'Victor',  'W': 'Whiskey',  'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'}

print([d[x] for x in name])


