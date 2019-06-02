from functools import partial
import elements
import globall
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Control(elements.DefineElements):
    buttons = []
    labels = []
    allButtons = []
    allLabels = []

    def __init__(self):
        super().__init__()
        globall.__init__(self)
        self.InitMe()

    def InitMe(self):
        self.label()
        self.button()
        self.input()

    def adjustOriginalElements(self):
        self.add1.move(20,50+25*(len(globall.paths)))
        self.add1.show()
        self.path0.move(50,50+25*(len(globall.paths)))
        self.path0.show()

    def remove(self,index):
        print(index)
        self.allButtons[index].hide()
        self.allLabels[index].hide()
        globall.delPaths.append(globall.paths[index])

    def manageDelete(self):
        for b in range(0,len(self.allButtons)):
            self.allButtons[b].clicked.connect(partial(self.remove,b))

    def mainUI(self):
        globall.newPaths = 0
        self.adjustOriginalElements()
        self.input.show()
        self.ddlist.show()
        self.search.show()
        self.dEdit.show()
        self.back.hide()
        self.add1.hide()
        self.path0.hide()
        self.save.hide()
        for btn in self.allButtons:
            btn.hide()
        for lb in self.allLabels:
            lb.hide()

    def directorySetup(self):
        self.dEdit.hide()
        self.input.hide()
        self.ddlist.hide()
        self.search.hide()
        self.back.show()
        self.save.show()
        if not globall.paths:
            self.add1.show()
            self.path0.show()
        else:
            self.buttons = []
            self.labels = []
            for i in range(1,len(globall.paths)+1):
                    self.buttons.append(QPushButton("",self))
                    self.allButtons.append(self.buttons[i-1])
                    self.buttons[i-1].setIcon(QIcon('assets\\minusbtn(100).png'))
                    self.buttons[i-1].move(20,50+(i-1)*25)
                    self.buttons[i-1].show()

                    self.labels.append(QLabel(self))
                    self.allLabels.append(self.labels[i-1])
                    self.labels[i-1].setFont(QFont("Roboto", 12))
                    self.labels[i-1].move(50,50+(i-1)*25)
                    self.labels[i-1].setStyleSheet("QLabel {font-style: italic;}")
                    self.labels[i-1].setText(globall.paths[i-1])
                    self.labels[i-1].adjustSize()
                    self.labels[i-1].show()
            self.manageDelete()
            self.adjustOriginalElements()
