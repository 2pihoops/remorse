# Borrowed morse lookup table from https://github.com/morse-talk/morse-talk/tree/master/morse_talk
# Thank you for not screaming at me.

import argparse
import collections

parser = argparse.ArgumentParser(description='Experience Regret over bygone encryptions')
parser.add_argument('message', type=str,
                    help='Message to handle')
parser.add_argument('--encrypt', dest='encrypt', action='store_true',
                    help='encrypt this message')

parser.add_argument('--decrypt', dest='decrypt', action='store_true',
                    help='decrypt this message')

parser.add_argument('--blank', type=str,
                    help='Decryption blank')
parser.add_argument('--hexblank', type=str,
                    help='Decryption blank in hex')

args = parser.parse_args()

morsetab = collections.OrderedDict([
    ('A', '01'),
    ('B', '1000'),
    ('C', '1010'),
    ('D', '100'),
    ('E', '0'),
    ('F', '0010'),
    ('G', '110'),
    ('H', '0000'),
    ('I', '00'),
    ('J', '0111'),
    ('K', '101'),
    ('L', '0100'),
    ('M', '11'),
    ('N', '10'),
    ('O', '111'),
    ('P', '0110'),
    ('Q', '1101'),
    ('R', '010'),
    ('S', '000'),
    ('T', '1'),
    ('U', '001'),
    ('V', '0001'),
    ('W', '011'),
    ('X', '1001'),
    ('Y', '1011'),
    ('Z', '1100'),
    ('0', '11111'),
    ('1', '01111'),
    ('2', '00111'),
    ('3', '00011'),
    ('4', '00001'),
    ('5', '00000'),
    ('6', '10000'),
    ('7', '11000'),
    ('8', '11100'),
    ('9', '11110'),
    (' ', '1111111'),
    (',', '110011'),
    ('.', '010101'),
    ('?', '001100'),
    (';', '101010'),
    (':', '111000'),
    ("'", '011110'),
    ('-', '100001'),
    ('/', '10010'),
    ('(', '101101'),
    (')', '101101'),
    ('_', '001101')
])
reversed_morsetab = {symbol: character for character, symbol in morsetab.items()}

blanktab = collections.OrderedDict([
    ('A', '10'),
    ('B', '1000'),
    ('C', '1000'),
    ('D', '100'),
    ('E', '1'),
    ('F', '1000'),
    ('G', '100'),
    ('H', '1000'),
    ('I', '10'),
    ('J', '1000'),
    ('K', '100'),
    ('L', '1000'),
    ('M', '10'),
    ('N', '10'),
    ('O', '100'),
    ('P', '1000'),
    ('Q', '1000'),
    ('R', '100'),
    ('S', '100'),
    ('T', '1'),
    ('U', '100'),
    ('V', '1000'),
    ('W', '100'),
    ('X', '1000'),
    ('Y', '1000'),
    ('Z', '1000'),
    ('0', '10000'),
    ('1', '10000'),
    ('2', '10000'),
    ('3', '10000'),
    ('4', '10000'),
    ('5', '10000'),
    ('6', '10000'),
    ('7', '10000'),
    ('8', '10000'),
    ('9', '10000'),
    (' ', '1000000'),
    (',', '100000'),
    ('.', '100000'),
    ('?', '100000'),
    (';', '100000'),
    (':', '100000'),
    ("'", '100000'),
    ('-', '100000'),
    ('/', '10000'),
    ('(', '100000'),
    (')', '100000'),
    ('_', '100000')
])

if args.encrypt:
    message = args.message
    output = ''
    blank = ''
    for c in message:
        output += morsetab[str.upper(c)]
        blank += blanktab[str.upper(c)]
    print("Encoded")
    print(output)
    print("Blank")
    print(blank)
    print("Encoded (hex)")
    print(hex(int('1111' + output, 2)))
    print("Blank (hex)")
    print(hex(int('1111' + blank, 2)))

if args.decrypt:
    blank = ''
    message = ''
    hexblank = ''

    if args.hexblank:
        hexblank = args.hexblank
        hexmessage = args.message
        message = bin(int(hexmessage,16))
        blank = bin(int(hexblank, 16))
        blank = blank.removeprefix('0b1111')
        message = message.removeprefix('0b1111')

    elif args.blank:
        blank = args.blank
        message = args.message
    # message and blank are binary numbers now.
    reading = False
    buffer = ''
    decrypted = ''


    for i in range(len(blank)):
        b = blank[i]
        c = message[i]
        if b == '1' and buffer != '':
            # lookup
            decrypted += reversed_morsetab[buffer]
            buffer = ''
        buffer += c
    decrypted += reversed_morsetab[buffer]
    print("Decrypted:")
    print(decrypted)
