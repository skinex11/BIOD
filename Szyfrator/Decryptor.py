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
#KOCHAMY CIEBIE BARDZO :) ZOSIA I KAROLINA <3<3<3<3
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

#Punkt 5 --------------------------------------------------------------------------------------------
    #w kazdym bloku przesuwamy nie parzyste pozycje na poprzednią nieparzystą pozycję
    for result in resultTable:
        #dla bloków 5-elementowych zmieniamy 3 pozycje
        if len(result) == 5:
            result[4], result[0], result[2] = result[0], result[2], result[4]
        #dla bloków 3 i 4 elementowych zmieniamy dwie pozycje
        elif 2 < len(result) < 5:
            result[2], result[0] = result[0], result[2]
        #dla bloków 1 i 2 elementowych nie robimy nic

