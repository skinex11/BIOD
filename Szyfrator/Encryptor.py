def encrypt(path, key):
    file = open(path, "r")
    content = file.read()
    file.close()

    #konwersja znaków na kody ASCII
    content = [ord(char) for char in content]
    key = [ord(char) for char in key]

    #odwracam klucz
    key.reverse()



def main():
    encrypt("plik.txt", "xyz-2")


if __name__ == '__main__':
    main()
