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
        resultTable[resultTable.index(result)] = [chr(code) for code in result]
    print(resultTable)




def main():
    encrypt("plik.txt", "xyz-2")


if __name__ == '__main__':
    main()
