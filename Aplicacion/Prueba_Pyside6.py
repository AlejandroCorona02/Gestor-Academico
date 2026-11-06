from PySide6.QtWidgets import * # Importo la libreria
from PySide6.QtCore import *
import sys # Importo el sys para poder ccerrar la ventana 

#Creo una funcion donde le estoy asignando un tamaño a la ventana
class Ventana1(QMainWindow):  # Usamos QMainWindow para que se comporte tal cual una ventana
    def setupUi(self):
        self.setFixedSize(500,500)
        self.setStyleSheet("background: #222222;") # Cambio el color del fondo, puedo usar nombres o directamente codigo hex
        
        """---------------------ESTA ES PARTE DEL 1ER FRAME------------------------------"""
        
        self.FRTitulo = QFrame(self) # Este frame es como un box de html donde se guardan datos y le podremos dar estilos, al usar self le decimos que usew la ventana1, esta a su vez usa window que a su vez es qmainwindow, basicamente es si mismo
        Cuadrado = QRect(10,10,480,200) # Generoo una variable justo por que se puede hacer de esta manera o directamente ponerla dentro de la funcion como argumento
        self.FRTitulo.setGeometry(Cuadrado) # Le damos un tamaño y donde inicia (x,y,h,w)
        self.FRTitulo.setStyleSheet("background: black;") # Aqui le decimos que de fondo deberia verse negro
        
        #Textos
        self.Titulo = QLabel(self.FRTitulo) # Aqui indicamos donde queremos que aparezca el texto, en este caso le indicamos que en el frame de texto
        self.Titulo.setText("Titriulos") # Aqui va el texto que queremos que tenga
        self.Titulo.setGeometry(QRect(10,10,460,40)) # Este es como un frame donde estan las palbras, pódemos decir que es un frame dentro de otro frame
        self.Titulo.setStyleSheet("""
                                  background: #222222;
                                  color: white;
                                  font-size: 25px;
                                  font-weight: bold;
                                  border-radius: 10px;
                                  """) # Podemos modificar todo el style lo podemose ver como un css, pues incluso maneja cosas similares
        self.Titulo.setAlignment(Qt.AlignCenter)
        
        
        """---------------------ESTA ES PARTE DEL 2DO FRAME------------------------------"""
        
        self.FRSubtitulos = QFrame(self)
        self.FRSubtitulos.setGeometry(QRect(10,220,480,200))
        self.FRSubtitulos.setStyleSheet("background: #FF0000;")
        
        self.Subtitulos = QLabel(self.FRSubtitulos)
        self.Subtitulos.setText("Ingresa algo")
        self.Subtitulos.setGeometry(QRect(10,10,460,40))
        self.Subtitulos.setStyleSheet("""
                                    background: #FF7070;
                                    color: #000000;
                                    font-size: 25px;
                                    font-weight: bold;
                                    border-radius: 10px;
                                    """)
        self.Subtitulos.setAlignment(Qt.AlignCenter)
        
        self.input = QLineEdit(self.FRSubtitulos)
        BoxPregunta = QRect(10,150,460,45)
        self.input.setGeometry(BoxPregunta)
        self.input.setStyleSheet("""
                                            background: #A70000;
                                            color: #ffffff;
                                            font-size: 25px;
                                            font-weight: bold;
                                            border-radius: 10px;
                                            """)
        
app = QApplication(sys.argv) # Crea la aplicación Qt y recibe los argumentos del programa.

window = Ventana1() # Creo una variable y le asigno la funcion de class
window.setupUi() # Mandamos llamar a la funcion de arriba
window.show() # Le dig que muestre la ventana

sys.exit(app.exec()) # mantiene la aplicación funcionando y permite responder a clics, teclas, cierres y demás interacciones.Hasta que manda la orden de cerrar