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

        #------INPUT DE TEXTO-----------
        # Aqui el input es un cuadro de texto donde podemos poner texto, pero podemos modificar incluso lo mismo
        self.input = QLineEdit(self.FRSubtitulos)
        BoxPregunta = QRect(10,100,460,45)
        self.input.setGeometry(BoxPregunta)
        self.input.setStyleSheet("""
                                            background: #A70000;
                                            color: #ffffff;
                                            font-size: 25px;
                                            font-weight: bold;
                                            border-radius: 10px;
                                            """)

        #----------BOTON---------------
        #Casi toodo es lo mismo, lo que cambia es que usamos un clicked para mandar llamar uan funcion 
        self.boton = QPushButton(self.FRSubtitulos)
        self.boton.setText("Adelante")
        Boton = QRect(200,150,100,45)
        self.boton.setGeometry(Boton)
        self.boton.setStyleSheet("""
                                    color: #000000;
                                    font-size: 20px;
                                    font-weight: bold;
                                    border: 2px solid #d70000;
                                    border-radius: 10px;
                                    background-color: #FF0000;
                                    """)
        self.boton.clicked.connect(self.ObtienesTexto)

        #------------Cuadro de dialogo-------------------------
        self.dialogo = QDialog(self)
        self.dialogo.setFixedSize(300,300)
        self.setStyleSheet("background: #222222;")

        #---------------Frames del dialogo---------------------------------
        self.FRtitulo_dialogo = QFrame(self.dialogo)
        self.FRtitulo_dialogo.setGeometry(QRect(10, 10, 280, 130))
        self.FRtitulo_dialogo.setStyleSheet("background: #ff5757;")

        # Textos en el cuadro de dialogo
        self.TitulDialogo = QLabel(self.FRtitulo_dialogo)
        self.TitulDialogo.setText("Cuadro de dialogo") 
        self.TitulDialogo.setGeometry(QRect(10,10,260,40)) 
        self.TitulDialogo.setStyleSheet("""
                                    background: #222222;
                                    color: white;
                                    font-size: 25px;
                                    font-weight: bold;
                                    border-radius: 10px;
                                    """)
        self.TitulDialogo.setAlignment(Qt.AlignCenter)

        self.FRSUBtitulo_dialogo = QFrame(self.dialogo)
        self.FRSUBtitulo_dialogo.setGeometry(QRect(10, 150, 280, 130))
        self.FRSUBtitulo_dialogo.setStyleSheet("background: #ff5757;")

        #-------Se abre una imagen en la ventana-----------------------
        self.Imagen = QFrame(self.FRSUBtitulo_dialogo)
        self.Imagen.setGeometry(QRect(10,10,260,110)) 
        self.Imagen.setStyleSheet("""
                                    border-image: url(Recursos/404.png) ;
                                    """)

    # Esta funciona es la que mando llamar, basicamente mando llamar el valor del texto que se encuentra en el frame del input y lo asigno a una variable, despues imprimo la variable
    def ObtienesTexto(self):
        self.dialogo.show() # Es para abrir la otra ventana que creamos
        texto = self.input.text()
        print(texto)
        
app = QApplication(sys.argv) # Crea la aplicación Qt y recibe los argumentos del programa.

window = Ventana1() # Creo una variable y le asigno la funcion de class
window.setupUi() # Mandamos llamar a la funcion de arriba
window.show() # Le dig que muestre la ventana

sys.exit(app.exec()) # mantiene la aplicación funcionando y permite responder a clics, teclas, cierres y demás interacciones.Hasta que manda la orden de cerrar