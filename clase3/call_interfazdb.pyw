import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from interfazdb import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateDB.clicked.connect(self.createDatabase)
        self.show()

    def createDatabase(self):
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".db")
            self.ui.labelResponse.setText("La base de datos se ha creado")
        except Error as e:
            self.ui.labelResponse.setText("Error al crear la base de datos")
        finally:
            conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


