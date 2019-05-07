from tkinter import *


def gui():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.input = StringVar()
            self.init_window()

        def onEncrypt(self, input):
            path = input.get()


        def  init_window(self):
            #tytuł okna
            self.master.title("Encryptor BIOD")

            #widget zajmuje całe okno
            self.pack(fill=BOTH, expand=1)

            #tworzenie text input
            pathInput = Entry(self, textvariable=self.input)
            pathInput.pack()

            #tworzenie buttona. Trzeba dodać comand=encrypt()
            browseButton = Button(self, text="Przeglądaj")
            encryptButton = Button(self, text="Encrypt", command=lambda: self.onEncrypt(self.input))
            decryptButton = Button(self, text="Decrypt")

            #umiejscowienie buttona
            browseButton.place(x=150, y=50)
            encryptButton.place(x=55, y=100)
            decryptButton.place(x=135, y=100)
            pathInput.place(x=10, y=55)

    root = Tk()
    #rozmiar okna
    root.geometry("220x200")

    app = Window(root)
    root.mainloop()
