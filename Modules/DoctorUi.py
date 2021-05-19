from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
sys.path.append("..")
import Modules.Icons_rc
from Modules import *
import os
from datetime import datetime

class DoctorUi_Window(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        self.ui = uic.loadUi(os.path.join(ui_path,"../Gui/DoctorUi.ui"), self)
        self.setWindowFlags(qtc.Qt.FramelessWindowHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.Center()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.newpatientflag  = 1
        self.dict = {}
        self.Window_size = 0
        self.Menu_status= 0

        # Navigation command buttons connections
        self.ui.btn_close.clicked.connect(self.Exit_command)
        self.ui.btn_restore.clicked.connect(self.restore_or_maximize_window)
        self.ui.btn_minimise.clicked.connect(self.showMinimized)

        self.ui.btn_menu.clicked.connect(self.Expand_Decrease_menu)
        self.ui.btn_home.clicked.connect(self.OpenHomePage)

        # new patient command buttons connections
        self.ui.btn_new.clicked.connect(self.OpenNewPatient)
        self.ui.Slider_Neut.valueChanged.connect(self.UpdateNeutLable)
        self.ui.Slider_Lymph.valueChanged.connect(self.UpdateLymphLable)
        self.ui.Slider_HCT.valueChanged.connect(self.UpdateHCTLable)
        self.ui.btn_accept.clicked.connect(self.OpenQuestnier)
        self.ui.btn_Continue.clicked.connect(self.OpenPrognosis)
        self.ui.btn_Finish_2.clicked.connect(self.FinishPatientDiagnosis)

        # patient history command buttons connections
        self.ui.btn_patient_history.clicked.connect(self.OpenPatientHistorySearch)
        self.ui.btn_find.clicked.connect(self.FindPatient)

        self.ui.radioButton__no.setChecked(True)
        self.ui.radioButton__no_2.setChecked(True)
        self.ui.radioButton__no_3.setChecked(True)
        self.ui.radioButton__no_4.setChecked(True)
        self.ui.radioButton__no_5.setChecked(True)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == qtc.Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.frame_top.mouseMoveEvent = moveWindow



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

    def OpenPatientHistorySearch(self):
        self.ui.lineEdit_Id_2.clear()
        self.ui.textEdit_prognosis_2.clear()
        self.ui.stackedWidget.setCurrentIndex(4)

    def OpenQuestnier(self):
        self.dict["WBC"] = self.ui.lineEdit_WBC.text()
        self.dict["Neut"] = self.ui.Slider_Neut.value()
        self.dict["Lymph"] = self.ui.Slider_Lymph.value()
        self.dict["RBC"] = self.ui.lineEdit_RBC.text()
        self.dict["HCT"] = self.ui.Slider_HCT.value()
        self.dict["Urea"] = self.ui.lineEdit_Urea.text()
        self.dict["Hb"] = self.ui.lineEdit_Hb.text()
        self.dict["Creatinine"] = self.ui.lineEdit_Creatinine.text()
        self.dict["Iron"] = self.ui.lineEdit_Iron.text()
        self.dict["HDL"] = self.ui.lineEdit_HDL.text()
        self.dict["AP"] = self.ui.lineEdit_AP.text()

        if CheckDictionaryValues(self.dict):
            self.dict["gender"] = self.ui.comboBox_Sex.currentText()
            self.newpatientflag = 2
            self.ui.stackedWidget.setCurrentIndex(self.newpatientflag)
            if self.dict["gender"] == 'M':
                self.ui.radioButton_yes_3.setEnabled(False)


    def OpenPrognosis(self):
        self.dict["Id"] = self.ui.lineEdit_Id.text()
        self.dict["origin"] = self.ui.comboBox_Ethnicity.currentText()
        self.dict["age"] = self.ui.lineEdit_Age.text()
        self.dict["smoker"] = self.ui.buttonGroup_Smokes.checkedButton().text()
        self.dict["Fever"] = self.ui.buttonGroup_Fever.checkedButton().text()
        self.dict["pregnancy"] = self.ui.buttonGroup_pregnant.checkedButton().text()
        self.dict["diarrhea"] = self.ui.buttonGroup_Diarrhea.checkedButton().text()
        self.dict["vomiting"] = self.ui.buttonGroup_Vomiting.checkedButton().text()

        if Check_Age_and_ID(self.dict):
            self.SavePatientfile()
            self.newpatientflag = 3
            self.ui.stackedWidget.setCurrentIndex(self.newpatientflag)

    def SavePatientfile(self):
        filepath = str(os.getcwd()) + "/Patient History"
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        full_path = completeName = os.path.join(filepath, self.dict["Id"] + ".txt")
        file = open(full_path, 'a')
        diagnosis = str(self.dict) + "\n"
        ConvertsValuesTo_LOW_HIGH_NORMAL(self.dict)
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        diagnosis = "\n\nDate: " + current_time + "\n" + diagnosis + "\n" + get_string_of_diagnosis_and_Treatment(get_diagnosis_dict(self.dict))
        file.writelines(diagnosis)
        self.ui.textEdit_prognosis.setText(diagnosis)
        file.close()

    def FinishPatientDiagnosis(self):
        self.ResetNewPatient()
        self.newpatientflag = 1
        self.ui.stackedWidget.setCurrentIndex(0)

    def ResetNewPatient(self):
        #new patient first page clear
        self.ui.comboBox_Sex.setCurrentIndex(0)
        self.ui.Slider_Neut.setValue(50)
        self.ui.Slider_Lymph.setValue(50)
        self.ui.Slider_HCT.setValue(50)
        self.ui.lineEdit_WBC.clear()
        self.ui.lineEdit_RBC.clear()
        self.ui.lineEdit_Urea.clear()
        self.ui.lineEdit_Hb.clear()
        self.ui.lineEdit_Creatinine.clear()
        self.ui.lineEdit_Iron.clear()
        self.ui.lineEdit_HDL.clear()
        self.ui.lineEdit_AP.clear()

        # new patient second page clear
        self.ui.comboBox_Ethnicity.setCurrentIndex(0)
        self.ui.lineEdit_Id.clear()
        self.ui.lineEdit_Age.clear()
        self.ui.radioButton__no.setChecked(True)
        self.ui.radioButton__no_2.setChecked(True)
        self.ui.radioButton__no_3.setChecked(True)
        self.ui.radioButton__no_4.setChecked(True)
        self.ui.radioButton__no_5.setChecked(True)

        # new patient prognosis page clear
        self.ui.textEdit_prognosis.clear()

    def FindPatient(self):
        Id = self.ui.lineEdit_Id_2.text()
        try:
            filepath = str(os.getcwd()) + "/Patient History"
            full_path = os.path.join(filepath, self.dict["Id"] + ".txt")
            file = open(full_path, 'r')
            self.ui.textEdit_prognosis_2.setText(file.read())

        except FileNotFoundError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setWindowTitle("Error")
            msg.setInformativeText('Id not found')
            msg.exec_()

    def UpdateNeutLable(self):
        text = str(self.ui.Slider_Neut.value()) + "%"
        self.ui.label_Neut_value.setText(text)

    def UpdateLymphLable(self):
        text = str(self.ui.Slider_Lymph.value()) + "%"
        self.ui.label_Lymph_value.setText(text)

    def UpdateHCTLable(self):
        text = str(self.ui.Slider_HCT.value()) + "%"
        self.ui.label_HCT_value.setText(text)

    def Expand_Decrease_menu(self):
        width = self.ui.frame_left_menu.width()
        if width == 70:
            newwidth = 210
        else:
            newwidth = 70
        self.animation = qtc.QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(qtc.QEasingCurve.InOutQuart)
        self.animation.start()


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


    def restore_or_maximize_window(self):
        win_status = self.Window_size
        if win_status == 0:
            self.btn_restore.setIcon(QtGui.QIcon(":/Icons/restore-window-128.png"))
            self.Window_size = 1
            self.showMaximized()
        else:
            self.btn_restore.setIcon(QtGui.QIcon(":/Icons/maximize-window-128.png"))
            self.Window_size = 0
            self.showNormal()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    UiWindow = DoctorUi_Window()
    UiWindow.show()
    app.exec_()