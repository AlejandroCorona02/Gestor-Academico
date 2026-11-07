from PySide6.QtWidgets import *
import sys


class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QStackedWidget") #Coloca nombre a la ventana
        self.resize(500, 300) # Coloca el tamaño fijo a una ventana

        # Contenedor de páginas
        self.stack = QStackedWidget()

        # Página 1
        pagina1 = QWidget()
        layout1 = QVBoxLayout()

        lbl1 = QLabel("Pantalla Principal")
        btn1 = QPushButton("Ir a Grupos")

        layout1.addWidget(lbl1)
        layout1.addWidget(btn1)

        pagina1.setLayout(layout1)

        # Página 2
        pagina2 = QWidget()
        layout2 = QVBoxLayout()

        lbl2 = QLabel("Pantalla de Grupos")
        btn2 = QPushButton("Regresar")

        layout2.addWidget(lbl2)
        layout2.addWidget(btn2)

        pagina2.setLayout(layout2)

        # Agregar páginas
        self.stack.addWidget(pagina1)  # índice 0
        self.stack.addWidget(pagina2)  # índice 1

        # Conexiones
        btn1.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        btn2.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        self.setCentralWidget(self.stack)


app = QApplication(sys.argv)

window = Ventana()
window.show()

sys.exit(app.exec())