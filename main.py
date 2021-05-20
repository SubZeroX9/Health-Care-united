from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys, os
sys.path.append("..")
from Modules import *
file_path = str(os.getcwd()) + "/Modules/Icons_rc.py"
if not os.path.exists(file_path):
    os.system('Pyrcc5 Images/Icons.qrc -o Modules/Icons_rc.py')

class UI(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginUi = Login_Register_Window()
        self.DoctorUi = DoctorUi_Window()
        self.loginUi.show()
        self.loginUi.LoginBtn.clicked.connect(self.Login_command)
        self.DoctorUi.ui.btn_Logout.clicked.connect(self.LogOut)
        sys.exit(app.exec_())


    def Login_command(self):
        user_id = self.loginUi.ui.IdLineEdit.text()
        user_name = self.loginUi.ui.UserNameLineEdit.text()
        password1 = self.loginUi.ui.PassLineEdit.text()
        if CheckLoginDetails(user_id, user_name, password1):
            self.loginUi.close()
            self.DoctorUi.show()

    def LogOut(self):
        self.loginUi.UserNameLineEdit.clear()
        self.loginUi.IdLineEdit.clear()
        self.loginUi.PassLineEdit.clear()
        self.DoctorUi.ui.stackedWidget.setCurrentIndex(0)
        self.DoctorUi.newpatientflag = 1
        self.DoctorUi.ResetNewPatient()
        self.DoctorUi.close()
        self.loginUi.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = UI()
