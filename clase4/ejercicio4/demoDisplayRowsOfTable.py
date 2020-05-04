# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDisplayRowsOfTable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(565, 427)
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
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.verticalLayout.addWidget(self.lineEditDBName)
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.verticalLayout.addWidget(self.lineEditTableName)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButtonDisplayRows = QtWidgets.QPushButton(Dialog)
        self.pushButtonDisplayRows.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDisplayRows.setFont(font)
        self.pushButtonDisplayRows.setStyleSheet("background-color: rgb(182, 199, 255);")
        self.pushButtonDisplayRows.setObjectName("pushButtonDisplayRows")
        self.verticalLayout_3.addWidget(self.pushButtonDisplayRows)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setStyleSheet("background-color: rgb(169, 255, 133);")
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout_3.addWidget(self.labelResponse)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Visualizando filas de una base de datos"))
        self.label.setText(_translate("Dialog", "Ingresar nombre de la base de datos"))
        self.label_2.setText(_translate("Dialog", "Ingresar nombre de la tabla"))
        self.pushButtonDisplayRows.setText(_translate("Dialog", "Mostrar filas"))

