import sys
from PyQt5           import  QtWidgets
from PyQt5.QtGui     import  QPixmap
from GUI_Main        import  Ui_MainWindow
from PyQt5.QtWidgets import  QFileDialog

import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array

class venta_principal(Ui_MainWindow):

	def __init__(self):
		pass
	
	def configuraciones( self, Ventana_Main):
		super().setupUi( Ventana_Main ) # con super class llamo al metodo setupUi de la clase Ui_Ventana_Main del file GUI.py
										# una vez se llama la metodo se pueden acceder ya a todos los parametros de configuracion
		
		self.pushButton_seleccionar.clicked.connect(self.getImage)
		self.pushButton_clasificar.clicked.connect(self.getClasification)


	def getImage(self):
		
		fname = QFileDialog.getOpenFileName(None, caption= 'Selecione una Imagen',directory='' ,filter="Image files (*.jpg *.gif *png)")
		self.imagePath = fname[0]
		pixmap = QPixmap(self.imagePath)
		pixmap = pixmap.scaled(480, 640)
		self.textBrowser_resultados.setText(" ")
		self.label_3.setPixmap(QPixmap(pixmap))
   
	def getClasification(self):
		
		img = self.load_image(self.imagePath)
		model = tf.keras.models.load_model('Modelo_Entrenado.h5')
		predictions = model.predict(img)

		if predictions==1:
			self.textBrowser_resultados.setText("La imagen corresponde a un PERRO")
		elif predictions==0:
			self.textBrowser_resultados.setText("La imagen corresponde a un GATO")
		else:
			self.textBrowser_resultados.setText("Error")

	def load_image(self, imagen):
		img = load_img(imagen, target_size=(150, 150))
		img = img_to_array(img)
		img = img.reshape(1, 150, 150, 3)
		img = img.astype('float32')
		return img






if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = venta_principal()
	ui.configuraciones(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())



