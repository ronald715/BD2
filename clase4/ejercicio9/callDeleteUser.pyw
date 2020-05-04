import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from demoDeleteUser import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDelete.clicked.connect(self.DeleteUser)
        self.ui.pushButtonYes.clicked.connect(self.ConfirmDelete)
        self.ui.labelSure.hide()
        self.ui.pushButtonYes.hide()
        self.ui.pushButtonNo.hide()
        self.show()
    def DeleteUser(self):
        selectStatement = "SELECT * FROM Usuarios where Correo like '"+self.ui.lineEditEmailAddress.text()+"'and Contraseña like'"+ self.ui.lineEditPassword.text() + "'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            cur.execute(selectStatement)
            row = cur.fetchone()
            if row == None:
                self.ui.labelSure.hide()
                self.ui.pushButtonYes.hide()
                self.ui.pushButtonNo.hide()
                self.ui.labelResponse.setText("El correo y la contraseña no coinciden, volver a intentarlo")
            else:
                self.ui.labelSure.show()
                self.ui.pushButtonYes.show()
                self.ui.pushButtonNo.show()
                self.ui.labelResponse.setText("")
        except Error as e:
            self.ui.labelResponse.setText("Hubo un error al acceder a la información del usuario")
        finally:
            conn.close()

    def ConfirmDelete(self):
        deleteStatement = "DELETE FROM Usuarios where Correo like '"+self.ui.lineEditEmailAddress.text()+"'and Contraseña like'"+ self.ui.lineEditPassword.text() + "'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            with conn:
                cur.execute(deleteStatement)
                self.ui.labelResponse.setText("Información de usuario eliminada correctamente")
        except Error as e:
            self.ui.labelResponse.setText("Hubo un error al eliminar la información del usuario")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

