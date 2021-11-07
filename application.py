import sys
import os

# from PySide2 import QtCore
from mainWin import *
from capturingFaces import *
from trainigRF import *
from recognitionFace import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView

# request
import requests
# url semilla apiRest
urlApi = 'http://control-personal.test/api/'

# Obteniendo los cargos y horarios
horariosCargos = requests.get(urlApi+'horarios-cargos')
dataHrsCrg = {}
if horariosCargos.status_code == 200:
    dataHrsCrg = horariosCargos.json()
    
# ejecutando la app
class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # table empleados
        self.ui.tabla_empleados.setColumnCount(5)
        self.ui.tabla_empleados.setHorizontalHeaderLabels(['Código', 'Empleado', 'Cargo', 'Estado', 'Rostro'])
        header = self.ui.tabla_empleados.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # llenado de tados en la tabla de empleados
        self.upListado()
        # end table empleados

        # items genero
        self.ui.combo_genero.addItem("--Seleccione género--")
        self.ui.combo_genero.addItem("Masculino")
        self.ui.combo_genero.addItem("Femenino")
        self.genero = ['', 'hombre', 'mujer']
        # end item genero

        # items cargo
        self.cargo = ['']
        self.ui.combo_cargo.addItem("--Seleccione cargo--")
        for item in dataHrsCrg['cargos']:
            self.ui.combo_cargo.addItem(
                item['nombre_cargo'] + ' - tarifa ' + str(item['tarifa']) + 'Bs.'
            )
            self.cargo.append(item['id'])
        # end items cargo

        # items horario
        self.horario = ['']
        self.ui.combo_horario.addItem("--Seleccione horario--")
        for item in dataHrsCrg['horarios']:
            tmpDescanso = ''
            if item['hora_descanso'] and item['hora_fin_descanso']:
                tmpDescanso = ' Descanso: ' + item['hora_descanso'] + ' - ' + item['hora_fin_descanso']
            self.ui.combo_horario.addItem(
                'Turno: ' + item['hora_inicio'] + ' - ' + item['hora_fin'] + tmpDescanso
            )
            self.horario.append(item['id'])
        # end items horario

        # boton de registro de empleado
        self.ui.btn_registrar.clicked.connect(self.registroUsuario)
        # QtCore.QObject.connect(self.ui.btnTraining, QtCore.SIGNAL("clicked()"), self.trainigModel)
        # QtCore.QObject.connect(self.ui.btnRecognition, QtCore.SIGNAL("clicked()"), self.recognitionUser)
    
    # funcion para el registro de empleado
    def registroUsuario(self):
        nombres = self.ui.in_nombres.text()
        apellidos = self.ui.in_apellidos.text()
        direccion = self.ui.in_direccion.text()
        tel_cel = self.ui.in_tel_cel.text()
        fecha_nacimiento = self.ui.in_fecha_nacimiento.text()
        combo_genero = self.genero[self.ui.combo_genero.currentIndex()]
        combo_cargo = self.cargo[self.ui.combo_cargo.currentIndex()]
        combo_horario = self.horario[self.ui.combo_horario.currentIndex()]
        
        if nombres=='' or apellidos=='' or direccion=='' or tel_cel=='' or fecha_nacimiento=='' or combo_genero=='' or combo_cargo=='' or combo_horario=='':
            QMessageBox.about(self, "Error", "Todos los datos son requeridos.")
        else:
            form = {
                'nombres': nombres,
                'apellidos': apellidos,
                'direccion': direccion,
                'tel_cel': tel_cel,
                'fecha_nacimiento': fecha_nacimiento,
                'genero': combo_genero,
                'cargo_id': combo_cargo,
                'horario_id':combo_horario
            }
            # envios de datos a la ApiRest
            x = requests.post(urlApi+'registro-empleado', data = form)
            if x.status_code == 400:
                QMessageBox.about(self, "Error", "Error con los tipos de datos, por favor revisa los datos nuevamente.")
            if x.status_code == 500:
                QMessageBox.about(self, "Error", "Problemas con el servidor, por favor vuelva a intentarlo mas tarde.")
            if x.status_code == 200:
                QMessageBox.about(self, "Bien hecho", "Empleado registrado con éxito.")
                self.ui.in_nombres.setText('')
                self.ui.in_apellidos.setText('')
                self.ui.in_direccion.setText('')
                self.ui.in_tel_cel.setText('')
                self.upListado()

    # funcion de listado de empleados
    def upListado(self):
        lista = requests.get(urlApi+'lista-empleados')
        empleados = []
        if lista.status_code == 200:
            empleados = lista.json()
            for i in range(self.ui.tabla_empleados.rowCount()):
                self.ui.tabla_empleados.removeRow(0)
        
        for empleado in empleados:
            # print(empleado)
            self.ui.tabla_empleados.insertRow(self.ui.tabla_empleados.rowCount())
            row = self.ui.tabla_empleados.rowCount() - 1
            self.ui.tabla_empleados.setItem(row, 0, QTableWidgetItem(empleado['cod_empleado']))
            self.ui.tabla_empleados.setItem(row, 1, QTableWidgetItem(empleado['nombres']+' '+empleado['apellidos']))
            self.ui.tabla_empleados.setItem(row, 2, QTableWidgetItem(empleado['cargo']['nombre_cargo']))
            self.ui.tabla_empleados.setItem(row, 3, QTableWidgetItem('Activo' if empleado['estado'] else 'Inactivo'))
            
            btn = QtWidgets.QPushButton(self)
            btn.setText('Capturar')
            btn.clicked.connect(lambda checked, arg=empleado['cod_empleado']: self.captureUser(arg))
            self.ui.tabla_empleados.setCellWidget(row, 4, btn)
    def captureUser(self, code):
        print(code)
        # nameUser = self.ui.name.text()
        # savePerson(nameUser, 'D:/project-python/RECONOCIMIENTO FACIAL/Data')
        savePerson(code, 'Data')
        # self.ui.successTxt.setText('Se guardo correctamente al empleado ' + nameUser)
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
