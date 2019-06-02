from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DefineElements(QWidget):
    windowX = 1600
    windowY = 50
    window_Width = 300
    window_Height = 400

    def label(self):
        self.path0 = QLabel(self)
        self.path0.setFont(QFont("Roboto", 12))
        self.path0.move(50,50)
        self.path0.setText("No Path")
        self.path0.setStyleSheet("QLabel {font-style: italic;}")
        self.path0.adjustSize()
        self.path0.hide()

    def point(self,posString,QPushButton):
        if posString == "topRight":
            pos = QPoint(self.window_Width - QPushButton.minimumSizeHint().width(),0)
        if posString == "bottomMiddle":
            pos = QPoint(self.window_Width/2 - QPushButton.minimumSizeHint().width()/2,)
        if posString == "bottomLeft":
            pos = QPoint(0,self.window_Height-QPushButton.minimumSizeHint().height()*2)
        return pos

    def button(self):
        self.dEdit = QPushButton("Add Directories",self)
        self.dEdit.move(self.point("topRight",self.dEdit))
        self.dEdit.show()

        self.add1 = QPushButton("",self)
        self.add1.setIcon(QIcon('assets\\plusIcon.jpg'))
        self.add1.move(20,50)
        self.add1.hide()

        self.back = QPushButton("<= Back",self)
        self.back.setMinimumSize(self.window_Width,50)
        self.back.hide()

        self.save = QPushButton("Save",self)
        self.save.move(self.point("bottomLeft",self.save))
        self.save.setMinimumSize(self.window_Width,50)
        self.save.hide()

        self.search = QPushButton("",self)
        self.search.move(self.window_Width-self.dEdit.minimumSizeHint().width()-self.search.minimumSizeHint().width(),0)
        self.search.setIcon(QIcon('assets\\mag(100).png'))
        self.search.show()

    def input(self):
        self.ddlist = QComboBox(self)
        self.ddlist.addItem("(...)")
        self.ddlist.resize(self.window_Width-self.dEdit.minimumSizeHint().width()-self.search.minimumSizeHint().width(),self.dEdit.minimumSizeHint().height())
        self.ddlist.show()

        self.input = QTextEdit(self)
        self.input.resize(self.window_Width-self.dEdit.minimumSizeHint().width()-self.search.minimumSizeHint().width(),self.dEdit.minimumSizeHint().height())
        self.input.show()
