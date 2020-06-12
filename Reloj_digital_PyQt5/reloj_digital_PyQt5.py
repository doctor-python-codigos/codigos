import sys
from PyQt5.QtGui     import QFont
from PyQt5.QtCore    import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QApplication,QVBoxLayout, QLabel

class Reloj_Display(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(840, 640)
        fnt = QFont('Helvetica [Cronyx]',100,QFont.Bold)
        layout = QVBoxLayout() 

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(fnt)

        layout.addWidget(self.lbl)
        self.setLayout(layout)
        timer = QTimer(self)
        timer.timeout.connect(self.mostrar_Tiempo)
        timer.start(1000) # actualizar cada segundo
        self.mostrar_Tiempo()
 
    def mostrar_Tiempo(self):
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm:ss')
        self.lbl.setText(displayTxt)

graph = QApplication(sys.argv)
reloj = Reloj_Display()
reloj.show()
graph.exit(graph.exec_())