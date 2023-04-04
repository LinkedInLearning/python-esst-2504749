def ausgabe_feld(feld_liste):
    print('-----------------')
    print(' ', feld_liste[0], ' | ', feld_liste[1], ' | ', feld_liste[2])
    print('-----------------')
    print(' ', feld_liste[3], ' | ', feld_liste[4], ' | ', feld_liste[5])
    print('-----------------')
    print(' ', feld_liste[6], ' | ', feld_liste[7], ' | ', feld_liste[8])
    print('-----------------')


def gewinn_abfrage(feld_liste, spieler):
    # Reihen
    if (feld_liste[0] == spieler) and (feld_liste[1] == spieler) and (feld_liste[2] == spieler):
        return True
    if (feld_liste[3] == spieler) and (feld_liste[4] == spieler) and (feld_liste[5] == spieler):
        return True
    if (feld_liste[6] == spieler) and (feld_liste[7] == spieler) and (feld_liste[8] == spieler):
        return True
    # Spalten
    if (feld_liste[0] == spieler) and (feld_liste[3] == spieler) and (feld_liste[6] == spieler):
        return True
    if (feld_liste[1] == spieler) and (feld_liste[4] == spieler) and (feld_liste[7] == spieler):
        return True
    if (feld_liste[2] == spieler) and (feld_liste[5] == spieler) and (feld_liste[8] == spieler):
        return True
    # Diagonalen
    if (feld_liste[0] == spieler) and (feld_liste[4] == spieler) and (feld_liste[8] == spieler):
        return True
    if (feld_liste[2] == spieler) and (feld_liste[4] == spieler) and (feld_liste[6] == spieler):
        return True
    
    return False


def abfrage_unentschieden(feld_liste):
    unentschieden = True
    for feld in feld_liste:
        if feld == ' ':
            unentschieden = False
    return unentschieden


# Das Feld ist eine Liste aus 9 Elementen
#---------------
# f0 | f1 | f2 |
# f3 | f4 | f5 |
# f6 | f7 | f8 |
#---------------

# Felder sind leer -> initialisieren mit Leerzeichen
spiel_feld = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


while True:
  # printe das Feld damit User:in sieht, welche Felder noch frei sind
  ausgabe_feld(spiel_feld)
  
  input_x = input('User:in x: waehle dein Feld und gib dafür die Zahl 1-9 ein: ')

  # setze das x an die richtige stelle:
  spiel_feld[int(input_x) - 1] = 'x'

  # Überprüfe ob user_x gewonnen hat
  sieg = gewinn_abfrage(spiel_feld, 'x')
  if sieg == True:
    print('Sieg X')
    break
  unentschieden = abfrage_unentschieden(spiel_feld)
  if unentschieden == True:
    print('Unentschieden')
    break

  # Das Gleiche muessen wir auch für den Kreis machen
  # printe das Feld damit User:in sieht, welche felder noch frei sind
  ausgabe_feld(spiel_feld)
  input_o = input('User:in o: wähle dein felde und gib dafür die Zahl 1-9 ein: ')

  # setze das o an die richtige stelle:
  spiel_feld[int(input_o) - 1] = 'o'
  
  # Überprüfe ob user_x gewonnen hat
  sieg = gewinn_abfrage(spiel_feld, 'o')
  if sieg == True:
    print('Sieg O')
    break


# Am Ende des Programms geben wir ein letztes Mal das Spielfeld aus
ausgabe_feld(spiel_feld)