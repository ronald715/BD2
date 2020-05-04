import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from demoSignInForm import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.SearchRows)
        self.show()
    def SearchRows(self):
        sqlStatement = "SELECT Correo, Contraseña FROM Usuarios where Correo like '"+self.ui.lineEditEmailAddress.text()+ "'and Contraseña like '" + self.ui.lineEditPassword.text()+"'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            cur.execute(sqlStatement)
            row = cur.fetchone()
            if row==None:
                self.ui.labelResponse.setText("Correo electrónico o contraseña equivocada, vuelve a intentarlo")
            else:
                self.ui.labelResponse.setText("Bienvenido a nuestro sistema :D")
        except Error as e:
            self.ui.labelResponse.setText("Hubo un error al acceder a la información")
        finally:
            conn.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())



