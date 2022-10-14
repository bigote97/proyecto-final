# Importamos opencv, libreria utilizada para analizar el codigo QR y extraer el dato decodificado en el
import cv2
from qrGenerator import generadorQR
#Definimos una funcion que recibira como parametro el path y nombre de la imagen que contiene el QR

def readQRCode(filename):
	try:
		# Intentamos leer la imagen
		img = cv2.imread(filename)
		# Detectamos el codigo QR que hay en la misma
		detect = cv2.QRCodeDetector()
		value, points, straight_qrcode = detect.detectAndDecode(img)
		# retornamos el dato obtenido
		return value
	except:
		# De no poder analizar la imagen devolvemos un mensaje de error
		# Estaria bueno trabajar sobre los posibles erroresd para ser mas claros con el usuario
		return 'error al abrir el archivo'


# Caso de prueba invocando la funcion "read_qr_code" para verificar que retorna se corresponde con el QR que se genera en "generadorQR"
generadorQR('prueba', 'Texto de prueba')
value = readQRCode('prueba.png')
print(value)