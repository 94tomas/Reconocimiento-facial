# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control-personal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 90, 781, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.lista_empleados = QtWidgets.QWidget()
        self.lista_empleados.setObjectName("lista_empleados")
        self.tabla_empleados = QtWidgets.QTableWidget(self.lista_empleados)
        self.tabla_empleados.setGeometry(QtCore.QRect(10, 20, 751, 431))
        self.tabla_empleados.setObjectName("tabla_empleados")
        self.tabla_empleados.setColumnCount(0)
        self.tabla_empleados.setRowCount(0)
        self.tabWidget.addTab(self.lista_empleados, "")
        self.registro_nuevo = QtWidgets.QWidget()
        self.registro_nuevo.setObjectName("registro_nuevo")
        self.gridLayoutWidget = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 361, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.nombres = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.nombres.setContentsMargins(0, 0, 0, 0)
        self.nombres.setObjectName("nombres")
        self.in_nombres = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.in_nombres.setObjectName("in_nombres")
        self.nombres.addWidget(self.in_nombres, 1, 0, 2, 1)
        self.la_nombres = QtWidgets.QLabel(self.gridLayoutWidget)
        self.la_nombres.setObjectName("la_nombres")
        self.nombres.addWidget(self.la_nombres, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(400, 30, 361, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.apellidos = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.apellidos.setContentsMargins(0, 0, 0, 0)
        self.apellidos.setObjectName("apellidos")
        self.in_apellidos = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.in_apellidos.setObjectName("in_apellidos")
        self.apellidos.addWidget(self.in_apellidos, 1, 0, 2, 1)
        self.la_apellidos = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.la_apellidos.setObjectName("la_apellidos")
        self.apellidos.addWidget(self.la_apellidos, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 110, 361, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.direccion = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.direccion.setContentsMargins(0, 0, 0, 0)
        self.direccion.setObjectName("direccion")
        self.in_direccion = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.in_direccion.setObjectName("in_direccion")
        self.direccion.addWidget(self.in_direccion, 1, 0, 2, 1)
        self.la_direccion = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.la_direccion.setObjectName("la_direccion")
        self.direccion.addWidget(self.la_direccion, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(400, 110, 361, 51))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.tel_cel = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.tel_cel.setContentsMargins(0, 0, 0, 0)
        self.tel_cel.setObjectName("tel_cel")
        self.in_tel_cel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.in_tel_cel.setObjectName("in_tel_cel")
        self.tel_cel.addWidget(self.in_tel_cel, 1, 0, 2, 1)
        self.la_tel_cel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.la_tel_cel.setObjectName("la_tel_cel")
        self.tel_cel.addWidget(self.la_tel_cel, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 190, 361, 51))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.fecha_nacimiento = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.fecha_nacimiento.setContentsMargins(0, 0, 0, 0)
        self.fecha_nacimiento.setObjectName("fecha_nacimiento")
        self.la_fecha_nacimiento = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.la_fecha_nacimiento.setObjectName("la_fecha_nacimiento")
        self.fecha_nacimiento.addWidget(self.la_fecha_nacimiento, 0, 0, 1, 1)
        self.in_fecha_nacimiento = QtWidgets.QDateEdit(self.gridLayoutWidget_5, calendarPopup=True)
        self.in_fecha_nacimiento.setDateTime(QtCore.QDateTime.currentDateTime())
        self.in_fecha_nacimiento.setObjectName("in_fecha_nacimiento")
        self.fecha_nacimiento.addWidget(self.in_fecha_nacimiento, 1, 0, 2, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(400, 190, 361, 51))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.genero = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.genero.setContentsMargins(0, 0, 0, 0)
        self.genero.setObjectName("genero")
        self.la_genero = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.la_genero.setObjectName("la_genero")
        self.genero.addWidget(self.la_genero, 0, 0, 1, 1)
        self.combo_genero = QtWidgets.QComboBox(self.gridLayoutWidget_6)
        self.combo_genero.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.combo_genero.setObjectName("combo_genero")
        self.genero.addWidget(self.combo_genero, 1, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(20, 270, 361, 51))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.cargo = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.cargo.setContentsMargins(0, 0, 0, 0)
        self.cargo.setObjectName("cargo")
        self.la_cargo = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.la_cargo.setObjectName("la_cargo")
        self.cargo.addWidget(self.la_cargo, 0, 0, 1, 1)
        self.combo_cargo = QtWidgets.QComboBox(self.gridLayoutWidget_7)
        self.combo_cargo.setObjectName("combo_cargo")
        self.cargo.addWidget(self.combo_cargo, 1, 0, 1, 1)
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.registro_nuevo)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(400, 270, 361, 51))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.horario = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.horario.setContentsMargins(0, 0, 0, 0)
        self.horario.setObjectName("horario")
        self.la_horario = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.la_horario.setObjectName("la_horario")
        self.horario.addWidget(self.la_horario, 0, 0, 1, 1)
        self.combo_horario = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        self.combo_horario.setObjectName("combo_horario")
        self.horario.addWidget(self.combo_horario, 1, 0, 1, 1)
        self.btn_registrar = QtWidgets.QPushButton(self.registro_nuevo)
        self.btn_registrar.setGeometry(QtCore.QRect(310, 360, 171, 51))
        self.btn_registrar.setStyleSheet("")
        self.btn_registrar.setObjectName("btn_registrar")
        self.tabWidget.addTab(self.registro_nuevo, "")
        self.btn_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iniciar.setGeometry(QtCore.QRect(310, 20, 201, 51))
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.btn_entrenar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrenar.setGeometry(QtCore.QRect(650, 60, 151, 31))
        self.btn_entrenar.setObjectName("btn_entrenar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lista_empleados), _translate("MainWindow", "Lista de empleados"))
        self.in_nombres.setPlaceholderText(_translate("MainWindow", "Juan"))
        self.la_nombres.setText(_translate("MainWindow", "Nombre(s)"))
        self.in_apellidos.setPlaceholderText(_translate("MainWindow", "Perez"))
        self.la_apellidos.setText(_translate("MainWindow", "Apellidos(s)"))
        self.in_direccion.setPlaceholderText(_translate("MainWindow", "Av. el maestro s/n"))
        self.la_direccion.setText(_translate("MainWindow", "Dirección"))
        self.in_tel_cel.setPlaceholderText(_translate("MainWindow", "61616161"))
        self.la_tel_cel.setText(_translate("MainWindow", "Tel/Cel"))
        self.la_fecha_nacimiento.setText(_translate("MainWindow", "Fecha de nacimiento"))
        self.la_genero.setText(_translate("MainWindow", "Género"))
        self.la_cargo.setText(_translate("MainWindow", "Cargo"))
        self.la_horario.setText(_translate("MainWindow", "Horario"))
        self.btn_registrar.setText(_translate("MainWindow", "Registrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.registro_nuevo), _translate("MainWindow", "Registro nuevo"))
        self.btn_iniciar.setText(_translate("MainWindow", "Iniciar asistencia"))
        self.btn_entrenar.setText(_translate("MainWindow", "Procesar imagenes"))