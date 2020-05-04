import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from demoChangePassword import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonChangePassword.clicked.connect(self.ChangePassword)
        self.show()

    def ChangePassword(self):
        selectStatement = "SELECT Correo, Contraseña FROM Usuarios where Correo like '"+self.ui.lineEditEmailAddress.text()+ "'and Contraseña like '"+self.ui.lineEditOldPassword.text() + "'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()
            cur.execute(selectStatement)
            row = cur.fetchone()
            if row == None:
                self.ui.labelResponse.setText("El correo y la contraseña no coinciden, volver a intentarlo")
            else:
                if self.ui.lineEditNewPassword.text()==self.ui.lineEditRePassword.text():
                    updateStatement = "UPDATE Usuarios set Contraseña = '" +self.ui.lineEditNewPassword.text()+ "' WHERE Correo like '"+self.ui.lineEditEmailAddress.text() + "'"
                    with conn:
                        cur.execute(updateStatement)
                    self.ui.labelResponse.setText("Contraseña cambiada correctamente")
                else:
                    self.ui.labelResponse.setText("Debes escribir la nueva contraseña de la misma manera en los dos últimos campos. Vuelve a intentarlo")
        except Error as e:
            self.ui.labelResponse.setText("Hubo un error al acceder a la información")
        finally:
            conn.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())



