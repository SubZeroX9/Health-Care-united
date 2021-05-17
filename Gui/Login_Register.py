from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
import os
sys.path.append("..")
from Modules import *

class Login_Register_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        self.ui = uic.loadUi(os.path.join(ui_path,"Login_RegisterForms.ui"), self)
        self.setWindowFlags(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.Center()
        self.ui.stackedWidget.setCurrentIndex(0)

        #Login page command connect
        self.ui.btn_close.clicked.connect(self.Exit_command)
        self.ui.RegisterBtn.clicked.connect(self.Register_command)

        #register page command connect
        self.ui.btn_close_2.clicked.connect(self.Exit_command)
        self.ui.RegisterBtn_2.clicked.connect(self.RegisterNewUser_command)
        self.ui.CancelBtn.clicked.connect(self.Cancel_command)

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
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Registered Succefuly")
            msg.setWindowTitle("Registered Succefuly")
            msg.setInformativeText("Registered Succefuly")
            self.ui.stackedWidget.setCurrentIndex(0)


    def Cancel_command(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def Exit_command(self):
        self.close()

    def Register_command(self):
        self.ui.stackedWidget.setCurrentIndex(1)




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = Login_Register_Window()
    UiWindow.show()
    app.exec_()