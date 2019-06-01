
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tkinter import *
from tkinter import filedialog

class Ui_Dialog(QWidget):
    path = None

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.l1 = QLabel(self)
        self.button = QPushButton("Search",self)

        self.setGeometry(1600,50,300,200)
        self.setWindowTitle("Fenster")
        self.button.clicked.connect(self.browse)

        self.l1.setFont(QFont("Calibri", 12))
        if self.path is None:
            self.l1.setText("No Path")
        self.l1.move(75,0)
        self.l1.setStyleSheet("QLabel {font-style: italic;}")
        self.show()

    def browse(self):
        self.path = filedialog.askdirectory()
        self.l1.setText(self.path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    sys.exit(app.exec_())

#QtCore.QMetaObject.connectSlotsByName(Dialog)
#def retranslateUi(self, Dialog):
#_translate = QtCore.QCoreApplication.translate
#Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
