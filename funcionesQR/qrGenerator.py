import pyqrcode

def generadorQR(nombre, id):
  # Generate QR code
	QR_Id = pyqrcode.create(id)
    
  # Create and save the png file naming "nombre.png"
	QR_Id.png(nombre + '.png', scale = 6)

	return nombre + '.png'