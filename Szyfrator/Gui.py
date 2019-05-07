from tkinter import *


def gui():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.init_window()

        def  init_window(self):
            #tytuł okna
            self.master.title("Encryptor BIOD")
            #widget zajmuje całe okno
            self.pack(fill=BOTH, expand=1)
            #tworzenie buttona
            browseButton = Button(self, text="Przeglądaj")
            encryptButton = Button(self, text="Encrypt")
            decryptButton = Button(self, text="Decrypt")
            #umiejscowienie buttona
            browseButton.place(x=300, y=50)
            encryptButton.place(x=115, y=200)
            decryptButton.place(x=195, y=200)

    root = Tk()
    #rozmiar okna
    root.geometry("400x300")

    app = Window(root)
    root.mainloop()
