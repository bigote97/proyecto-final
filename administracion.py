# Desde aqui se administraran todas las acciones respecto a las plantas:
# Buscar, agregar, modificar, eliminar

from traceback import print_list
from numpy import true_divide
from planta import Planta
from repositorioPlantas import Repositorio
from funcionesQR import qrReader
from funcionesQR import qrReaderFile
from funcionesQR import qrGenerator

class Administrador:
  def __init__(self, listado_plantas = []):
    #self.repositorio = Repositorio()
    self.plantas = listado_plantas
  
  def agregarPlanta(self, id, planta, tipo, siembra = "otra", cosecha = "otro"):
    planta = Planta(id, planta, tipo, siembra, cosecha)
    self.plantas.append(planta)
    repo = Repositorio()
    repo.guardarPlantas(self.plantas)
    return planta

  def buscarxTexto(self, filtro):
    return [ planta for planta in self.plantas if planta.coincide(filtro) ]

  def buscarID(self, id_planta):
    for planta in self.plantas:
      if str(planta.id) == str(id_planta):
        return planta
    return None

  def eliminarPlanta(self, id_planta):
    planta = self._buscar_por_id(id_planta)
    if planta:
      self.plantas.remove(planta)
      Repositorio.guardar_plantas(self.plantas)
      return True
    return False

  def modificarPlanta(self, id_planta, tipo, fec_cosecha):
    planta = self.buscarID(id_planta)
    if planta:
      planta.texto = tipo
      planta.cosecha = fec_cosecha
      repo = Repositorio()
      repo.guardarPlantas(self.plantas)
      return True
    return False

  def analizarQRCamara(self):
    scan = qrReader.scanQRCode()
    if scan == 'ErrorCode:01-No hay camara':
      scan = qrReaderFile.readQRCode('prueba.png')
    return scan
  
  def analizarQRImagen(self, ruta):
    scan = qrReaderFile.readQRCode(ruta)
    return scan
  
  def generarQR(self, nombre, id):
    QR = qrGenerator.generadorQR(nombre, id)
    return QR
  
  def cargarTipos(self):
    lista_tipos=[]
    for planta in self.plantas:
      if not planta.tipo in lista_tipos:
        lista_tipos.append(planta.tipo)
    return lista_tipos
    
# Codigo de prueba para las funciones de QR.
# Primero generamos un QR para probar que esta funcion este ok, y de paso ya contar
# con uno para hacer las pruebas de los casos de disponer camara, o no hacerlo
#admin = Administrador()
#QR = admin.generarQR('prueba', 'ID:4543')
#print(QR)
#scan = admin.analizarQRCamara()
#if scan == 'ErrorCode:01-No hay camara':
#  scan = admin.analizarQRImagen(QR)
#print(scan)