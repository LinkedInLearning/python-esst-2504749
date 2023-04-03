variable_1 = 5
variable_2 = 6

if (variable_1 == variable_2):
    print('Beide Variablen sind gleich gross.')


variable_3 = 3

if (variable_1 == variable_2) and (variable_3 > variable_2):
    print('Bedingung and erfuellt.')

if (variable_1 == variable_2) or (variable_3 > variable_2):
    print('Bedingung or erfuellt.')

if not (variable_3 > variable_2):
    print('Bedingung not erfuellt.')


###### else if 04
variable_1 = 5
variable_2 = 6
variable_3 = 2

if (variable_1 == variable_2):
    print('Beide Variablen sind gleich gross.')
else:
    print('Die Variablen sind nicht gleich gross.')


if (variable_1 == variable_2):
    print('Beide Variablen sind gleich gross.')
elif (variable_3 < 4):
    print('Die Variablen sind nicht gleich gross und variable 3 ist kleiner als 4')
else:
    print('Keine der Bedignungen ist erfuellt.')


###### for 05

meine_zahlen = [0,10,50]
for meine_zahl in meine_zahlen:
    print('Die Zahl ist ', meine_zahl)


for index in range(3):
    print('Die Zahl ist ', meine_zahlen[index])



###### while 06
meine_var = 2
while ( meine_var < 20 ):
    print('variable :',  meine_var)
    meine_var = meine_var * 2 

