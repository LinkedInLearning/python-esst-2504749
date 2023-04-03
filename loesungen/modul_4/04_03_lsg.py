# Challenge 1

def ausgabe_meine_liste(meine_liste):
    for element in meine_liste:
        print('Element', element)

test_liste = [1,2,3,4]
ausgabe_meine_liste(test_liste)


#Challenge 2
def meine_berechnung(parameter_1, parameter_2):
    ergebnis = parameter_1 * (parameter_2 + 2)
    return ergebnis

test_parameter_1 = 2
test_parameter_2 = 3
test_ergebnis = meine_berechnung(test_parameter_1, test_parameter_2)
print('Test Ergebnist ist', test_ergebnis)


# Challenge 3
def mein_check(parameter_1, parameter_2, parameter_3):
    if (parameter_1 < parameter_2) and (parameter_2 < parameter_3):
        return True
    else:
        return False

test_parameter_1 = 2
test_parameter_2 = 3
test_parameter_3 = 4
test_ergebnis = mein_check(test_parameter_1, test_parameter_2, test_parameter_3)
print('Das ergebnis des Checks ist ', test_ergebnis)