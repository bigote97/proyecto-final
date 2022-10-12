
# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  

def generadorQR(nombre, id):
  # Generate QR code
  url = pyqrcode.create(id)
    
  # Create and save the png file naming "myqr.png"
  url.png(nombre + '.png', scale = 6)

generadorQR('nombre', 14)