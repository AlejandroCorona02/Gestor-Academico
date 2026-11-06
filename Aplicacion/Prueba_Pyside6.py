from PySide6.QtWidgets import * # Importo la libreria
from PySide6.QtCore import *
import sys # Importo el sys para poder ccerrar la ventana 

#Creo una funcion donde le estoy asignando un tamaño a la ventana
class Ventana1(QMainWindow):  # Usamos QMainWindow para que se comporte tal cual una ventana
    def setupUi(self):
        self.setFixedSize(500,500)
        self.setStyleSheet("background: #222222;") # Cambio el color del fondo, puedo usar nombres o directamente codigo hex
        
        self.frame1 = QFrame(self) # Este frame es como un box de html donde se guardan datos y le podremos dar estilos, al usar self le decimos que usew la ventana1, esta a su vez usa window que a su vez es qmainwindow, basicamente es si mismo
        Cuadrado = QRect(10,10,480,200) # Generoo una variable justo por que se puede hacer de esta manera o directamente ponerla dentro de la funcion como argumento
        self.frame1.setGeometry(Cuadrado) # Le damos un tamaño y donde inicia (x,y,h,w)
        self.frame1.setStyleSheet("background: black;") # Aqui le decimos que de fondo deberia verse negro
        
        self.frame2 = QFrame(self)
        self.frame2.setGeometry(QRect(10,220,480,200))
        self.frame2.setStyleSheet("background: #ff0000;")
                
app = QApplication(sys.argv) # Crea la aplicación Qt y recibe los argumentos del programa.

window = Ventana1() # Creo una variable y le asigno la funcion de class
window.setupUi() # Mandamos llamar a la funcion de arriba
window.show() # Le dig que muestre la ventana

sys.exit(app.exec()) # mantiene la aplicación funcionando y permite responder a clics, teclas, cierres y demás interacciones.Hasta que manda la orden de cerrar