from tkinter import *
from tkinter.filedialog import askopenfilename


def gui():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.inputPath = StringVar()
            self.inputKey = StringVar()
            self.pathInput = Entry(self)
            self.keyInput = Entry(self)
            self.init_window()

        def onBrowse(self):
            path = askopenfilename()
            self.pathInput.delete(0, 'end')
            self.pathInput.insert(0, path)

        def onEncrypt(self, inputPath, inputKey):
            self.inputPath = inputPath.get()
            self.inputKey = inputKey.get()
            self.quit()


        def  init_window(self):
            #tytuł okna
            self.master.title("Encryptor BIOD")

            #widget zajmuje całe okno
            self.pack(fill=BOTH, expand=1)

            #tworzenie text input
            self.pathInput.configure(textvariable=self.inputPath, width=50)
            self.pathInput.insert(0, "Ścieżka do pliku")
            self.pathInput.pack()

            self.keyInput.configure(textvariable=self.inputKey, width=50, show="*")
            self.keyInput.insert(0, "Klucz szyfru")
            self.keyInput.pack()

            #tworzenie buttona. Trzeba dodać comand=encrypt()
            browseButton = Button(self, text="Przeglądaj", command=self.onBrowse)
            encryptButton = Button(self, text="Encrypt", command=lambda: self.onEncrypt(self.inputPath, self.inputKey))
            decryptButton = Button(self, text="Decrypt")
            infoButton = Button(self, text="?")

            #umiejscowienie
            browseButton.place(x=330, y=10)
            encryptButton.place(x=135, y=100)
            decryptButton.place(x=215, y=100)
            self.pathInput.place(x=10, y=15)
            self.keyInput.place(x=10, y=50)

    root = Tk()
    #rozmiar okna
    root.geometry("420x200")

    app = Window(root)
    root.mainloop()
    return app.pathInput, app.keyInput
