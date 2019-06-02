import sys
from os import listdir
import os
import subprocess
import globall
from functools import partial
import win32com.client
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tkinter import *
from tkinter import filedialog
import ui_control


class Ui_Dialog(ui_control.Ui_Control):
    x = __import__('elements').DefineElements.windowX
    y = __import__('elements').DefineElements.windowY
    w = __import__('elements').DefineElements.window_Width
    h = __import__('elements').DefineElements.window_Height
    files = []
    names = []

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(self.x,self.y,self.w,self.h)
        self.setWindowTitle("SoftSearcher")
        self.events()
        self.show()

    def events(self):
        self.dEdit.clicked.connect(self.directorySetup)
        self.add1.clicked.connect(self.browse)
        self.save.clicked.connect(self.mainUI)
        self.back.clicked.connect(self.cancel)
        self.search.clicked.connect(self.searching)

    def browse(self):
        path = filedialog.askdirectory()
        if path is None:
            self.path0.setText("No Path")
        else:
            self.path0.adjustSize()
            globall.newPaths += 1
            globall.paths.append(path)
            self.directorySetup()

    def cancel(self):
        globall.delPaths = []
        for x in range(0,globall.newPaths):
            globall.paths.pop()
        self.mainUI()

    def searching(self):
        for n in range (1,len(self.names)):
            self.ddlist.removeItem(n)
        if self.ddlist.currentText() != "(...)":
            self.ddlist.removeItem(self.ddlist.currentIndex())
        self.names = []
        self.files = []
        s = self.input.toPlainText()
        if s:
            if globall.paths:
                self.search.setToolTip("Search for Files")
                for dir in globall.paths:
                    self.getFiles(dir)
                for name in self.names:
                    print(name)
                    if name.startswith(str(s)):
                        self.ddlist.addItem(name)
                        self.ddlist.activated[int].connect(partial(self.launch,name))
                self.ddlist.showPopup()
                print("einmal")
            else:
                self.search.setToolTip("No directories defined; Click on \'Add Directories\' to add them")

    @pyqtSlot(int)
    def launch(self,index):
        print(index)
        for n in range(0,len(self.names)):
            if index == self.names[n]:
                subprocess.call([self.files[n]])


    def getFiles(self,input):
        for f in listdir(input):
            if os.path.isfile(os.path.join(input,f)):
                if f.endswith(".exe"): #evtl. Option for custom type scope
                    self.files.append(os.path.join(input,f))
                    self.names.append(f)
                if f.endswith(".lnk"):
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(os.path.join(input,f))
                    self.files.append(shortcut.Targetpath)
                    self.names.append(f)
            elif os.path.isdir(os.path.join(input,f)):
                self.getFiles(os.path.join(input,f))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    sys.exit(app.exec_())

#QtCore.QMetaObject.connectSlotsByName(Dialog)
#def retranslateUi(self, Dialog):
#_translate = QtCore.QCoreApplication.translate
#Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
