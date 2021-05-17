from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
sys.path.append("..")
from Modules import *
import os

class DoctorUi_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        self.ui = uic.loadUi(os.path.join(ui_path,"DoctorUi.ui"), self)
        self.setWindowFlags(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.Center()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.newpatientflag  = 1
        self.dict = {}


        self.ui.btn_close.clicked.connect(self.Exit_command)

        self.ui.btn_new.clicked.connect(self.OpenNewPatient)
        self.ui.btn_home.clicked.connect(self.OpenHomePage)
        self.ui.btn_patient_history.clicked.connect(self.OpenPatientHistory)
        self.ui.btn_menu.clicked.connect(self.Manu_Expand_minimise)



    def Center(self):
        qr = self.frameGeometry()
        cp = qtw.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Exit_command(self):
        self.close()

    def OpenNewPatient(self):
        self.ui.stackedWidget.setCurrentIndex(self.newpatientflag)

    def OpenHomePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def OpenPatientHistory(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def Manu_Expand_minimise(self):
        return

    def OpenQuestnier(self):
        dict["WBC"] = self.ui.lineEdit_WBC.text()
        #dict["Neut"] = self.ui.FullNameLineEdit.text()
        #dict["Lymph"] = self.ui.FullNameLineEdit.text()
        dict["RBC"] = self.ui.lineEdit_RBC.text()
        #dict["HCT"] = self.ui.FullNameLineEdit.text()
        dict["Urea"] = self.ui.lineEdit_Urea.text()
        dict["Hb"] = self.ui.lineEdit_Hb.text()
        dict["Creatinine"] = self.ui.lineEdit_Creatinine.text()
        dict["Iron"] = self.ui.lineEdit_Iron.text()
        dict["HDL"] = self.ui.lineEdit_HDL.text()
        dict["AP"] = self.ui.lineEdit_AP.text()




        if CheckDictionaryValues():
            self.newpatientflag = 2
            self.ui.stackedWidget.setCurrentIndex(2)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = DoctorUi_Window()
    UiWindow.show()
    app.exec_()