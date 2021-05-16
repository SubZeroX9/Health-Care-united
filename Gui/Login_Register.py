from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
sys.path.append("..")
from Modules import *

class Login_Register_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = uic.loadUi("Login_RegisterForms.ui", self)
        self.setWindowFlags(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.ui.btn_close.clicked.connect(self.Exit_command)
        self.ui.btn_close_2.clicked.connect(self.Exit_command)
        self.ui.RegisterBtn.clicked.connect(self.Register_command)
        self.Center()
        self.ui.RegisterBtn_2.clicked.connect(self.RegisterNewUser_command)

    def Center(self):
        qr = self.frameGeometry()
        cp = qtw.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def RegisterNewUser_command(self):
        user_id = self.ui.IdLineEdit_2.text()
        user_name = self.ui.UserNameLineEdit_2.text()
        password1 = self.ui.PassLineEdit_2.text()
        password2 = self.ui.ConfirmPassLineEdit.text()
        full_name = self.ui.FullNameLineEdit.text()

        if(CheckRegistrationDetails(user_id, user_name, password1, password2,full_name)):
            self.ui.stackedWidget.setCurrentIndex(0)

    def Cancel_command(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def Exit_command(self):
        self.close()

    def Register_command(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    #def Login_command(self):

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = Login_Register_Window()
    UiWindow.show()
    app.exec_()