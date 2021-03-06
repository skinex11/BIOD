def decrypt(path, key, resultFileName):
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
    file = open(path, "r", encoding="ISO-8859-1")
    #odczytujemy zawartość
    content = file.read()
    content = list(content)
    content.reverse()
    contentTable = [content[i:i+5] for i in range(0, len(content), 5)]

#Punkt 5 --------------------------------------------------------------------------------------------
    #w kazdym bloku przesuwamy nie parzyste pozycje na poprzednią nieparzystą pozycję
    for content in contentTable:
        #dla bloków 5-elementowych zmieniamy 3 pozycje
        if len(content) == 5:
            content[4], content[0], content[2] = content[0], content[2], content[4]
        #dla bloków 3 i 4 elementowych zmieniamy dwie pozycje
        elif 2 < len(content) < 5:
            content[2], content[0] = content[0], content[2]
        #dla bloków 1 i 2 elementowych nie robimy nic

#Punkt 4 -------------------------------------------------------------------------------------------
    #zamieniamy znaki na kody ASCII
    for content in contentTable:
        contentTable[contentTable.index(content)] = [ord(char) for char in content]

#Punkt 3 -------------------------------------------------------------------------------------------
    for content in contentTable:
        result = []
        #dla każdego bloku obliczamy różnicę znaku szyfrowanego i klucza
        for i in range(0, len(content)):
            diff = content[i]-key[i]
            result.append(diff if diff > 0 else diff+256)
        #dodajemy odszyfrowany blok do zbiorczej tablicy
        resultTable.append(result)

    for result in resultTable:
        resultTable[resultTable.index(result)] = [chr(char) for char in result]

#Punkt 2 -----------------------------------------------------------------------------
    if len(resultFileName) is 0:
        resultFileName = "decryption.txt"

    resultFile = open(resultFileName, "w+", encoding="ISO-8859-1")
    for result in resultTable:
        for i in range(0, len(result)):
            resultFile.write(result[i])
    resultFile.close()