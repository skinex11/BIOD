from tkinter import *
from tkinter.filedialog import askopenfilename


def gui():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.input = StringVar()
            self.pathInput = Entry(self)
            self.init_window()

        def onBrowse(self):
            path = askopenfilename()
            self.pathInput.insert(0, path)

        def onEncrypt(self, input):
            path = input.get()
            print(path)


        def  init_window(self):
            #tytuł okna
            self.master.title("Encryptor BIOD")

            #widget zajmuje całe okno
            self.pack(fill=BOTH, expand=1)

            #tworzenie text input
            self.pathInput.configure(textvariable=self.input)
            self.pathInput.pack()

            #tworzenie buttona. Trzeba dodać comand=encrypt()
            browseButton = Button(self, text="Przeglądaj", command=self.onBrowse)
            encryptButton = Button(self, text="Encrypt", command=lambda: self.onEncrypt(self.input))
            decryptButton = Button(self, text="Decrypt")

            #umiejscowienie buttona
            browseButton.place(x=150, y=50)
            encryptButton.place(x=55, y=100)
            decryptButton.place(x=135, y=100)
            self.pathInput.place(x=10, y=55)

    root = Tk()
    #rozmiar okna
    root.geometry("220x200")

    app = Window(root)
    root.mainloop()
