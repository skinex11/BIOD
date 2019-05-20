import os

from Gui import gui


def encrypt(path, key, resultFileName):
    resultTable = []
    contentTable = []
    # konwersja klucza na kody ASCII
    key = [ord(char) for char in key]
    # dopełniam klucz do 5
    extend = 0
    while len(key) < 5:
        key.append(key[extend])
        extend += 1
    # odwracam klucz
    key.reverse()

# Punkt 6 ----------------------------------------------------------------------------------------------
    #otwieramy plik
    file = open(path, "r")
    while True:
        #odczytujemy 5 znaków z pliku
        content = file.read(5)

        #jeżeli są znaki to dodajemy do tablicy zbiorczej
        if content:
            contentTable.append(content)
        # jeżeli nie ma znaków to zamykamy plik
        else:
            file.close()
            break

    #odwracamy szyfrogram
    contentTable.reverse()
    for content in contentTable:
        content.reverse()

