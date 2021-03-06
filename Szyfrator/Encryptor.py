import os

def encrypt(path, key, resultFileName):
    resultTable = []
    contentTable = []
    #konwersja klucza na kody ASCII
    key = [ord(char) for char in key]
    #dopełniam klucz do 5
    extend = 0
    while len(key) < 5:
        key.append(key[extend])
        extend += 1
    # odwracam klucz
    key.reverse()

#Punkt 2 -------------------------------------------------------------------------------------------
    #otwieramy plik
    file = open(path, "r")
    while True:
        #odczytujemy 5 znaków z pliku
        content = file.read(5)

        #jeżeli są znaki to dodajemy do tablicy zbiorczej
        if content:
            #konwersja znaków na kody ASCII
            content = [ord(char) for char in content]
            contentTable.append(content)
        # jeżeli nie ma znaków to zamykamy plik
        else:
            file.close()
            break

#Punkt 3 -------------------------------------------------------------------------------------------
    for content in contentTable:
        result = []
        #dla każdego bloku obliczamy sumę znaku szyfrowanego i klucza
        for i in range(0, len(content)):
            sum = key[i]+content[i]
            result.append(sum if sum < 256 else sum-256)
        #dodajemy zaszyfrowany blok do zbiorczej tablicy
        resultTable.append(result)

#Punkt 4 -------------------------------------------------------------------------------------------
    #zamieniamy kody ASCII na znaki
    for result in resultTable:
        resultTable[resultTable.index(result)] = [chr(code) for code in result]

#Punkt 5 --------------------------------------------------------------------------------------------
    #w kazdym bloku przesuwamy nie parzyste pozycje na następną nieparzystą pozycję
    for result in resultTable:
        #dla bloków 5-elementowych zmieniamy 3 pozycje
        if len(result) == 5:
            result[0], result[2], result[4] = result[4], result[0], result[2]
        #dla bloków 3 i 4 elementowych zmieniamy dwie pozycje
        elif 2 < len(result) < 5:
            result[0], result[2] = result[2], result[0]
        #dla bloków 1 i 2 elementowych nie robimy nic

#Punkt 6 ----------------------------------------------------------------------------------------------
    #odwracamy tablice wynikową
    for result in resultTable:
        result.reverse()
    resultTable.reverse()

    #tworzymy plik wynikowy
    if len(resultFileName) is 0:
        resultFileName = "result.txt"

    resultFile = open(resultFileName, "w+", encoding="ISO-8859-1")
    for result in resultTable:
        for i in range(0, len(result)):
            resultFile.write(result[i])
    resultFile.close()

    #usuwanie pliku oryginalnego
    os.remove(path)
