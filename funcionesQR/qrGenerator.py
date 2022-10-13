
# Import QRCode from pyqrcode
import pyqrcode  

def generadorQR(nombre, id):
  # Generate QR code
  QR_Id = pyqrcode.create(id)
    
  # Create and save the png file naming "myqr.png"
  QR_Id.png(nombre + '.png', scale = 6)


# Dejo este fragmento de codigo para testear de manera unitaria la generacion de codigos QR
generadorQR('Juan-berta', '141234234234234234234')