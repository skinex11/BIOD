def encrypt(path, key):
    file = open(path, "r")
    content = file.read()
    file.close()




def main():
    encrypt("plik.txt", "xyz-2")


if __name__ == '__main__':
    main()
