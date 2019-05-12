from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


def gui():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.inputPath = StringVar()
            self.pathInput = Entry(self)

            self.inputKey = StringVar()
            self.keyInput = Entry(self)

            self.inputResult = StringVar()
            self.resultInput = Entry(self)

            self.init_window()

        def onBrowse(self):
            path = askopenfilename()
            self.pathInput.insert(0, path)

        def onEncrypt(self, inputPath, inputKey, inputResult):
            self.inputPath = inputPath.get()
            self.inputKey = inputKey.get()
            self.inputResult = inputResult.get()
            self.quit()

        def onInfo(self):
            messagebox.showinfo("Okienko pomocy",
                                "Szyfrator BIOD\n"
                                "W pierszym polu podaj ścieżkę do pliku\n"
                                "W drugim klucz szyfrowania\n"
                                "Wybierz czy chcesz szyfrować czy odszyfrować\n"
                                "Plik wynikowy pojawi się w tej samej lokalizacji co wykonywany program\n"
                                "Autor: Patryk Konopka")

        def init_window(self):
            #tytuł okna
            self.master.title("Encryptor BIOD")

            #widget zajmuje całe okno
            self.pack(fill=BOTH, expand=1)

            #tworzenie text input
            self.pathInput.configure(textvariable=self.inputPath, width=50)
            labelPath = Label(self, text="Ścieżka do pliku: ")
            self.pathInput.pack()

            self.keyInput.configure(textvariable=self.inputKey, width=50, show="*")
            labelKey = Label(self, text="Klucz szyfrujacy: ")
            self.keyInput.pack()

            self.resultInput.configure(textvariable=self.inputResult, width=25, show="")
            labelResult = Label(self, text="Nazwa pliku wynikowego: ")
            self.resultInput.pack()

            #tworzenie buttona
            browseButton = Button(self, text="Przeglądaj", command=self.onBrowse)
            encryptButton = Button(self, text="Encrypt", command=lambda: self.onEncrypt(self.inputPath,
                                                                                        self.inputKey,
                                                                                        self.inputResult))
            decryptButton = Button(self, text="Decrypt")
            infoButton = Button(self, text="HELP", command=self.onInfo)

            #umiejscowienie
            labelPath.place(x=10, y=15)
            self.pathInput.place(x=110, y=15)
            browseButton.place(x=430, y=10)

            labelKey.place(x=10, y=50)
            self.keyInput.place(x=110, y=50)

            labelResult.place(x=10, y=85)
            self.resultInput.place(x=160, y=85)

            encryptButton.place(x=185, y=135)
            decryptButton.place(x=265, y=135)

            infoButton.place(x=460, y=170)

    root = Tk()
    #rozmiar okna
    root.geometry("520x200")

    app = Window(root)
    root.mainloop()
    return app.pathInput.get(), app.keyInput.get(), app.resultInput.get()
