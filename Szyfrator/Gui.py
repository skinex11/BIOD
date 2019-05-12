from tkinter import *
from tkinter import messagebox
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
            self.pathInput.insert(0, path)

        def onEncrypt(self, inputPath, inputKey):
            self.inputPath = inputPath.get()
            self.inputKey = inputKey.get()
            self.quit()

        def onInfo(self):
            messagebox.showinfo("Okienko pomocy",
                                "Szyfrator BIOD\n"
                                "W pierszym polu podaj ścieżkę do pliku\n"
                                "W drugim klucz szyfrowania\n"
                                "Wybierz czy chcesz szyfrować czy odszyfrować\n"
                                "Plik wynikowy pojawi się w tej samej lokalizacji co wykonywany program\n"
                                "Autor: Patryk Konopka")

        def  init_window(self):
            #tytuł okna
            self.master.title("Encryptor BIOD")

            #widget zajmuje całe okno
            self.pack(fill=BOTH, expand=1)

            #tworzenie text input
            self.pathInput.configure(textvariable=self.inputPath, width=50)
            self.pathInput.pack()

            self.keyInput.configure(textvariable=self.inputKey, width=50, show="*")
            self.keyInput.pack()

            labelPath = Label(self, text="Ścieżka do pliku: ")
            labelKey = Label(self, text="Klucz szyfrujacy: ")

            #tworzenie buttona. Trzeba dodać comand=encrypt()
            browseButton = Button(self, text="Przeglądaj", command=self.onBrowse)
            encryptButton = Button(self, text="Encrypt", command=lambda: self.onEncrypt(self.inputPath, self.inputKey))
            decryptButton = Button(self, text="Decrypt")
            infoButton = Button(self, text="HELP", command=self.onInfo)

            #umiejscowienie
            browseButton.place(x=430, y=10)
            encryptButton.place(x=185, y=100)
            decryptButton.place(x=265, y=100)
            infoButton.place(x=460, y=170)
            labelPath.place(x=10, y=15)
            labelKey.place(x=10, y=50)
            self.pathInput.place(x=110, y=15)
            self.keyInput.place(x=110, y=50)

    root = Tk()
    #rozmiar okna
    root.geometry("520x200")

    app = Window(root)
    root.mainloop()
    return app.pathInput.get(), app.keyInput.get()
