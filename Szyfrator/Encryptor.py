def encrypt(path, key):
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

        #jeżeli nie to zamykamy plik
        else:
            file.close()
            break


        # file.close()
        #
        # #konwersja znaków na kody ASCII
        # content = [ord(char) for char in content]
        #
        #
        # for i in range()

def main():
    encrypt("plik.txt", "xyz-2")


if __name__ == '__main__':
    main()
