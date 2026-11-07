from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Menu(QMainWindow):

    def setup_ui(self):
        self.rootLayout = QVBoxLayout() # Esta es la funcion que creara la ventana de manera que se pueda cmabiar el tamaño por el usuario, ademas el QVBoxLayout indica como se organizaran los widgets que se agregan, este es de arriba hacia abajo
        #self.rootLayout = QHBoxLayout() # Este es de izquierda a derecha
        #self.rootLayout = QGridLayout() # Este es por celdas, y para agregar el widgets se necesita indicar fila y columna
        #self.rootLayout = QFormLayout() # Se usa para los formularios 
        #self.rootLayout = QStackedLayout() # Permite tener varias paginas y mostrar solo una 
        #self.rootLayout = QSplitter() # Es como lista de izquierda a derecha pero el usuario lo puede acomodar
        self.frameTitulo = QFrame()
        self.frameInputs = QFrame()

        self.frameTitulo.setStyleSheet("background: red;")
        self.frameInputs.setStyleSheet("background: blue;")

        #Aqui agregamos los frames que creamos al Widget esto para que las figuras se acomoden de manera automatica a la ventana, el numero indica el procentaje de la ventana que abarcara cada uno
        self.rootLayout.addWidget(self.frameTitulo,20)
        self.rootLayout.addWidget(self.frameInputs,80)

        self.widget = QWidget()
        self.widget.setLayout(self.rootLayout)

        self.setCentralWidget(self.widget)


import sys

app = QApplication(sys.argv)

menu = Menu()
menu.setup_ui()
menu.show()

sys.exit(app.exec())