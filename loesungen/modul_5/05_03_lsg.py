import random

user_zug = input('Gib Schere, Stein oder Papier ein: ')
print('Spieler waehlt', user_zug)

computer_waehlt = random.randint(0, 3)
if computer_waehlt == 0:
    computer_zug = 'Schere'
elif computer_waehlt == 1:
    computer_zug = 'Stein'
else:
    computer_zug = 'Papier'
print('Computer waehlt', computer_zug)


if (user_zug == computer_zug):
    print('Unentschieden')

if (user_zug == 'Schere') and (computer_zug == 'Papier'):
    print('Spieler gewinnt.')
if (computer_zug == 'Schere') and (user_zug == 'Papier'):
    print('Computer gewinnt.')

if (user_zug == 'Schere') and (computer_zug == 'Stein'):
    print('Computer gewinnt.')
if (user_zug == 'Stein') and (computer_zug == 'Schere'):
    print('Spieler gewinnt.')

if (user_zug == 'Papier') and (computer_zug == 'Stein'):
    print('Spieler gewinnt.')
if (user_zug == 'Stein') and (computer_zug == 'Papier'):
    print('Computer gewinnt.')