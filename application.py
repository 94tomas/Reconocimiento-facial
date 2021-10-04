import sys
import os

# from PySide2 import QtCore
from mainWin import *
from capturingFaces import *
from trainigRF import *
from recognitionFace import *
from PyQt5.QtWidgets import QApplication, QMainWindow

# request
import requests
urlApi = 'http://control-personal.test/api/'
horariosCargos = requests.get(urlApi+'horarios-cargos')
dataHrsCrg = {}
if horariosCargos.status_code == 200:
    dataHrsCrg = horariosCargos.json()

# app = QApplication(sys.argv)
# window = QDialog()
# ui = Ui_Dialog()
# ui.setupUi(window)

# window.show()
# sys.exit(app.exec_())

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # items genero
        self.ui.combo_genero.addItem("--Seleccione género--")
        self.ui.combo_genero.addItem("Masculino")
        self.ui.combo_genero.addItem("Femenino")
        # end item genero

        # items cargo
        self.ui.combo_cargo.addItem("--Seleccione cargo--")
        for item in dataHrsCrg['cargos']:
            self.ui.combo_cargo.addItem(
                item['nombre_cargo'] + ' - tarifa ' + str(item['tarifa']) + 'Bs.'
            )
        # end items cargo

        # items horario
        self.ui.combo_horario.addItem("--Seleccione horario--")
        for item in dataHrsCrg['horarios']:
            tmpDescanso = ''
            if item['hora_descanso'] and item['hora_fin_descanso']:
                tmpDescanso = ' Descanso: ' + item['hora_descanso'] + ' - ' + item['hora_fin_descanso']
            self.ui.combo_horario.addItem(
                'Turno: ' + item['hora_inicio'] + ' - ' + item['hora_fin'] + tmpDescanso
            )
        # end items horario

        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.dateedit, QtCore.Qt.TopLeftCorner)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())


    #     QtCore.QObject.connect(self.ui.btnCapture, QtCore.SIGNAL("clicked()"), self.captureUser)
    #     QtCore.QObject.connect(self.ui.btnTraining, QtCore.SIGNAL("clicked()"), self.trainigModel)
    #     QtCore.QObject.connect(self.ui.btnRecognition, QtCore.SIGNAL("clicked()"), self.recognitionUser)
    
    # def captureUser(self):
    #     nameUser = self.ui.name.text()
    #     # savePerson(nameUser, 'D:/project-python/RECONOCIMIENTO FACIAL/Data')
    #     savePerson(nameUser, '/Data')
    #     self.ui.successTxt.setText('Se guardo correctamente al empleado ' + nameUser)
    # def trainigModel(self):
    #     # mainTrainig('D:/project-python/RECONOCIMIENTO FACIAL/Data')
    #     mainTrainig('/Data')
    #     self.ui.trainingTxt.setText('Entrado para reconocer')
    # def recognitionUser(self):
    #     # mainRecognition('D:/project-python/RECONOCIMIENTO FACIAL/Data')
    #     mainRecognition('/Data')
    #     self.ui.successTxt.setText('')
    #     self.ui.trainingTxt.setText('')


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())    
