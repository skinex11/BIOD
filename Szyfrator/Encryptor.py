from Gui import gui


def encrypt(path, key):
    resultTable = []
    contentTable = []
    #konwersja klucza na ASCII
    key = [ord(char) for char in key]
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
            result.append(key[i]+content[i])
        #dodajemy zaszyfrowany blok do zbiorczej tablicy
        resultTable.append(result)

#Punkt 4 -------------------------------------------------------------------------------------------
    #zamieniamy kody ASCII na znaki
    for result in resultTable:
        #print(chr(130).encode("cp1250").decode("cp1250"))
        resultTable[resultTable.index(result)] = [chr(code) for code in result]
    print(resultTable)

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
    resultFile = open("result.txt", "w+", encoding="Windows=1250")
    for result in resultTable:
        for i in range(0, len(result)):
            char = result[i].encode().decode("Windows-1250")
            resultFile.write(char)
    resultFile.close()


def main():
    gui()
    #encrypt("plik.txt", "xyz-2")


if __name__ == '__main__':
    main()
