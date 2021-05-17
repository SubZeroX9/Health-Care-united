from Gui import *
from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
sys.path.append("..")
from Modules import *


class UI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginUi = Login_Register_Window()
        self.DoctorUi = DoctorUi_Window()
        self.loginUi.show()
        app.exec_()

        self.loginUi.ui.LoginBtn.clicked.connect(self.Login_command)
        self.DoctorUi.ui.btn_Logout.clicked.connect(self.LogOut)


    def Login_command(self):
        user_id = self.loginUi.ui.IdLineEdit.text()
        user_name = self.loginUi.ui.UserNameLineEdit.text()
        password1 = self.loginUi.ui.PassLineEdit.text()
        if CheckLoginDetails(user_id, user_name, password1):
            self.loginUi.close()
            self.DoctorUi.show()

    def LogOut(self):
        self.DoctorUi.close()
        self.loginUi.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = UI()
