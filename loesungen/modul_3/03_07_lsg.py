# Challenge 1

meine_liste = [0, 0, 0, 0, 0]

# weise den 3x Wert des Index zu
for index in range(5):
    meine_liste[index] = index * 3

# Gebe nur Werte aus die groesser als 6 sind
for element in meine_liste:
    if element > 6:
        print('Element ', element)


# Challenge 2
erste_variable = 10
zweite_variable = 2

while (zweite_variable <= erste_variable):
    erste_variable = erste_variable + 1
    zweite_variable = zweite_variable + 2

print('Zweite Variable das erste Mal groeser als die erste Variable')
print('Erste Variable:', erste_variable)
print('Zweite Variable:', zweite_variable)




