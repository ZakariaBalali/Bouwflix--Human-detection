
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox


# importing all the functions defined in main.py
from HumanDetection import *

class Ui_Bouwflix(object):

    #variable of the folder where the video's are and path where the cutvideo will be stored
    uploadPath=""
    destinationPath=""

    def setupUi(self, Bouwflix):
        Bouwflix.setObjectName("Bouwflix")
        Bouwflix.resize(782, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Bouwflix.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Bouwflix)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_Upload = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_Upload.setGeometry(QtCore.QRect(40, 130, 341, 121))
        self.gb_Upload.setObjectName("gb_Upload")
        self.btn_OpenFolder = QtWidgets.QPushButton(self.gb_Upload, clicked=lambda: self.openFolder_dialog())
        self.btn_OpenFolder.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.btn_OpenFolder.setObjectName("btn_OpenFolder")
        self.lbl_GeselecteerdeFolder = QtWidgets.QLabel(self.gb_Upload)
        self.lbl_GeselecteerdeFolder.setGeometry(QtCore.QRect(20, 60, 201, 51))
        self.lbl_GeselecteerdeFolder.setWordWrap(True)
        self.lbl_GeselecteerdeFolder.setObjectName("lbl_GeselecteerdeFolder")
        self.lbl_Titel = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Titel.setGeometry(QtCore.QRect(290, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("SF Pro Black")
        font.setPointSize(26)
        self.lbl_Titel.setFont(font)
        self.lbl_Titel.setObjectName("lbl_Titel")
        self.lbl_Info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Info.setGeometry(QtCore.QRect(120, 60, 541, 51))
        self.lbl_Info.setScaledContents(False)
        self.lbl_Info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_Info.setWordWrap(True)
        self.lbl_Info.setObjectName("lbl_Info")
        self.gp_Output = QtWidgets.QGroupBox(self.centralwidget)
        self.gp_Output.setGeometry(QtCore.QRect(420, 130, 331, 251))
        self.gp_Output.setObjectName("gp_Output")
        #DIT MOET NOG GEFIXT WORDEN. De output van de terminal moet geredirect worden naar de textbrowser
        self.textBrowser_Output = QtWidgets.QTextBrowser(self.gp_Output)
        self.textBrowser_Output.setGeometry(QtCore.QRect(20, 40, 291, 171))
        self.textBrowser_Output.setObjectName("textBrowser_Output")
        self.btn_Start = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.evt_btnStart_clicked())
        self.btn_Start.setGeometry(QtCore.QRect(110, 440, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Start.setFont(font)
        self.btn_Start.setObjectName("btn_Start")
        font = QtGui.QFont()
        font.setPointSize(7)
        self.gp_Opslaan = QtWidgets.QGroupBox(self.centralwidget)
        self.gp_Opslaan.setGeometry(QtCore.QRect(40, 260, 341, 121))
        self.gp_Opslaan.setObjectName("gp_Opslaan")
        self.btn_OpslaanAls = QtWidgets.QPushButton(self.gp_Opslaan, clicked=lambda: self.saveAs_dialog())
        self.btn_OpslaanAls.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.btn_OpslaanAls.setObjectName("btn_OpslaanAls")
        self.lbl_BestemmingsFolder = QtWidgets.QLabel(self.gp_Opslaan)
        self.lbl_BestemmingsFolder.setGeometry(QtCore.QRect(20, 60, 321, 51))
        self.lbl_BestemmingsFolder.setWordWrap(True)
        self.lbl_BestemmingsFolder.setObjectName("lbl_BestemmingsFolder")
        self.gb_Progressie = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_Progressie.setGeometry(QtCore.QRect(420, 390, 331, 161))
        self.gb_Progressie.setObjectName("gb_Progressie")
        self.prgBar = QtWidgets.QProgressBar(self.gb_Progressie)
        self.prgBar.setGeometry(QtCore.QRect(90, 70, 118, 23))
        self.prgBar.setProperty("value", 0)
        self.prgBar.setObjectName("prgBar")
        self.lbl_Progress = QtWidgets.QLabel(self.gb_Progressie)
        self.lbl_Progress.setGeometry(QtCore.QRect(90, 100, 201, 16))
        self.lbl_Progress.setObjectName("lbl_Progress")
        Bouwflix.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bouwflix)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 26))
        self.menubar.setObjectName("menubar")
        Bouwflix.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bouwflix)
        self.statusbar.setObjectName("statusbar")
        Bouwflix.setStatusBar(self.statusbar)

        self.retranslateUi(Bouwflix)
        QtCore.QMetaObject.connectSlotsByName(Bouwflix)

    def retranslateUi(self, Bouwflix):
        _translate = QtCore.QCoreApplication.translate
        Bouwflix.setWindowTitle(_translate("Bouwflix", "Bouwflix"))
        self.gb_Upload.setTitle(_translate("Bouwflix", "Upload"))
        self.btn_OpenFolder.setText(_translate("Bouwflix", "Open Folder..."))
        self.lbl_GeselecteerdeFolder.setText(_translate("Bouwflix", "Geen folder gekozen"))
        self.lbl_Titel.setText(_translate("Bouwflix", "Bouwflix."))
        self.lbl_Info.setText(_translate("Bouwflix","Deze applicatie verwijderd dode momenten uit video\'s van bouwplaatsen die van binnen uit zijn gefilmd."))
        self.gp_Output.setTitle(_translate("Bouwflix", "Output"))
        self.btn_Start.setText(_translate("Bouwflix", "Start"))
        self.btn_Start.setDisabled(True)
        self.gp_Opslaan.setTitle(_translate("Bouwflix", "Opslaan als"))
        self.btn_OpslaanAls.setText(_translate("Bouwflix", "Opslaan als..."))
        self.lbl_BestemmingsFolder.setText(_translate("Bouwflix", "Geen bestmmings folder gekozen"))
        self.gb_Progressie.setTitle(_translate("Bouwflix", "Progressie"))
        self.lbl_Progress.setText(_translate("Bouwflix", "Applicatie is nog niet gestart"))
        self.statusbar.showMessage("Om te starten moet er eerst een folder(met daarin video's) en een bestemmings folder worden gekozen" )

    def openFolder_dialog(self):
        self.uploadPath = str(QFileDialog.getExistingDirectory(None, "Select Directory"))

        # Writing path under the button if a folder is selected
        if self.uploadPath != "":
            self.lbl_GeselecteerdeFolder.setText(self.uploadPath)

             #if the video's folder is also selected. enable start button
            if self.destinationPath != "":

                self.btn_Start.setDisabled(False)

                # message which is shown in bottom statusbar
                self.statusbar.showMessage(f"Druk op start om de video's in de '{self.uploadPath}' te bewerken. ")


    def saveAs_dialog(self):
        self.destinationPath = str(QFileDialog.getSaveFileName(None, "Save as",directory='.', filter="Video File (*.mp4)")[0])
        
        # Writing path under the button if a folder is selected
        if self.destinationPath != "":
            self.lbl_BestemmingsFolder.setText(self.destinationPath)

            #if the video's folder is also selected. enable start button
            if self.uploadPath != "":

                self.btn_Start.setDisabled(False)

                # message which is shown in bottom statusbar
                self.statusbar.showMessage(f"Druk op start om de video's in de '{self.uploadPath}' te bewerken. ")


    # This method is used to start the Humandetection as a backgroundThread, so that the PYQT gui does not say 'not-responding'
    def evt_btnStart_clicked(self):
        self.btn_Start.setDisabled(True)
        self.worker = MainBackgroundThread(self.uploadPath, self.destinationPath)
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.update_progress.connect(self.evt_update_progress)
        self.worker.current_state.connect(self.evt_current_state)
        self.worker.output.connect(self.evt_update_textedit)
        # message which is shown in bottom statusbar
        self.statusbar.showMessage(f"De applicatie is gestart. Dit kan even duren. Een moment geduld aub")

    def evt_worker_finished(self):
        self.btn_Start.setDisabled(False)
        self.statusbar.showMessage(f"Video staat klaar in '{self.destinationPath}'")
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap("finished.png"))
        msg.setWindowIcon(QtGui.QIcon('finished.png'))
        msg.setText("Klaar!")
        msg.setInformativeText("Alle video's zijn bewerkt.")
        msg.setWindowTitle("Klaar!")
        msg.exec_()

    def evt_update_progress(self, val):
        self.prgBar.setValue(val)

    def evt_current_state(self, state):
        self.lbl_Progress.setText(state)

    def evt_update_textedit(self, val):
        self.textBrowser_Output.append(val)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bouwflix = QtWidgets.QMainWindow()
    ui = Ui_Bouwflix()
    ui.setupUi(Bouwflix)
    Bouwflix.show()
    
    sys.exit(app.exec_())

