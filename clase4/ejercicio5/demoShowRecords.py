# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoShowRecords.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 444)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.verticalLayout.addWidget(self.lineEditEmailAddress)
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonFirst = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFirst.setFont(font)
        self.pushButtonFirst.setObjectName("pushButtonFirst")
        self.horizontalLayout_2.addWidget(self.pushButtonFirst)
        self.pushButtonPrevious = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPrevious.setFont(font)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.horizontalLayout_2.addWidget(self.pushButtonPrevious)
        self.pushButtonNext = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNext.setFont(font)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        self.pushButtonLast = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLast.setFont(font)
        self.pushButtonLast.setObjectName("pushButtonLast")
        self.horizontalLayout_2.addWidget(self.pushButtonLast)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setMaximumSize(QtCore.QSize(16777215, 200))
        self.labelResponse.setStyleSheet("background-color: rgb(253, 158, 248);")
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout_3.addWidget(self.labelResponse)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Navegando a través de filas de una base de datos"))
        self.label.setText(_translate("Dialog", "Correo Electrónico"))
        self.label_2.setText(_translate("Dialog", "Contraseña"))
        self.pushButtonFirst.setText(_translate("Dialog", "Primera fila"))
        self.pushButtonPrevious.setText(_translate("Dialog", "Anterior"))
        self.pushButtonNext.setText(_translate("Dialog", "Siguiente"))
        self.pushButtonLast.setText(_translate("Dialog", "Última fila"))

