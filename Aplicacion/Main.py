from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys

class Aplicacion(QMainWindow):
    def setup_ui(self):
        self.setWindowTitle("Gestor Academico")

        self.GrupoPaginas = QStackedWidget()

        #Pagina Principal
        Principal = QWidget()
        LayoutP = QVBoxLayout()
        TituloP = QLabel("Bienvenido")
        LayoutP.addWidget(TituloP)
        Principal.setLayout(LayoutP)
        self.GrupoPaginas.addWidget(Principal)
        self.setCentralWidget(self.GrupoPaginas)
    
app = QApplication(sys.argv)
window = Aplicacion()
window.show()

sys.exit(app.exec())
