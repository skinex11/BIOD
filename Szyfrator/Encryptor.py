def encrypt(path, key):
    resultTable = []
    #konwersja klucza na ASCII
    key = [ord(char) for char in key]
    # odwracam klucz
    key.reverse()

    #otwieramy plik
    file = open(path, "r")
    while True:
        #odczytujemy 5 znaków z pliku
        content = file.read(5)

        #jeżeli są znaki to szyfrujemy
        if content:
            result = []
            #konwersja znaków na kody ASCII
            content = [ord(char) for char in content]

            #sumujemy wartości kluczy ASCII klucza i tekstu
            for i in range(0, len(content)):
               result.append(key[i]+content[i])

            #dodajemy wartości ASCII jednego bloku do zbiorczej tablicy
            resultTable.append(result)

        #jeżeli nie ma znaków to zamykamy plik
        else:
            file.close()
            break


def main():
    encrypt("plik.txt", "xyz-2")


if __name__ == '__main__':
    main()
