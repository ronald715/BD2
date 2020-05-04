import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from demoSearchRows import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.SearchRows)
        self.show()
    def SearchRows(self):
        sqlStatement = "SELECT Contraseña FROM "+self.ui.lineEditTableName.text()+" where Correo like'"+self.ui.lineEditEmailAddress.text()+"'"
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".db")
            cur = conn.cursor()
            cur.execute(sqlStatement)
            row = cur.fetchone()
            if row==None:
                self.ui.labelResponse.setText("No encontramos ningún usuario con este correo electrónico. Lo sentimos T.T")
                self.ui.lineEditPassword.setText("")
            else:
                self.ui.labelResponse.setText("Correo electrónico encontrado, la contraseña de este usuario es: ")
                self.ui.lineEditPassword.setText(row[0])
        except Error as e:
            self.ui.labelResponse.setText("Hubo un error al acceder a la fila")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())