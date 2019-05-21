from PyQt5.QtWidgets import *
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Plik do zaszyfrowania:")
        self.label.move(10,22)

        self.btn = QPushButton('Przeglądaj', self)
        self.btn.move(270, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 22)

        self.label2 = QLabel(self)
        self.label2.setText("Klucz:")
        self.label2.move(90, 52)

        self.le2 = QLineEdit(self)
        self.le2.move(120, 52)

        self.btn = QPushButton('Szyfruj', self)
        self.btn.move(90, 82)
        self.btn.clicked.connect(self.showDialog)

        self.btn = QPushButton('Deszyfruj', self)
        self.btn.move(180, 82)
        self.btn.clicked.connect(self.showDialog)

        self.setGeometry(500, 330, 350, 110)
        self.setWindowTitle('Szyfrator BIOD')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())