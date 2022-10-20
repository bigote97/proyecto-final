# Desde aqui se administraran todas las acciones respecto a las plantas:
# Buscar, agregar, modificar, eliminar

from datetime import date, datetime
from traceback import print_list
from numpy import true_divide
from planta import Planta
from repositorioPlantas import Repositorio

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
    return [ planta for planta in self.plantas if planta.existePlanta(filtro) ]

  def buscarID(self, id_planta):
    for planta in self.plantas:
      if str(planta.id) == str(id_planta):
        return planta
    return None

  def eliminarPlanta(self, id_planta):
    planta = self.buscarID(id_planta)
    if planta:
      self.plantas.remove(planta)
      repo = Repositorio()
      repo.guardarPlantas(self.plantas)
      return True
    return False

  def modificarPlanta(self, id_planta, tipo, fec_cosecha):
    planta = self.buscarID(id_planta)
    if planta:
      planta.tipo = tipo
      planta.cosecha = date(fec_cosecha)
      repo = Repositorio()
      repo.guardarPlantas(self.plantas)
      return True
    return False

  def cargarTipos(self):
    lista_tipos=[]
    # cambiar a set
    for planta in self.plantas:
      if not planta.tipo in lista_tipos:
        lista_tipos.append(planta.tipo)
    return lista_tipos
    
# Codigo de prueba para las funciones de QR.
# Primero generamos un QR para probar que esta funcion este ok, y de paso ya contar
# con uno para hacer las pruebas de los casos de disponer camara, o no hacerlo
# admin = Administrador()
#QR = admin.generarQR('prueba', 'ID:4543')
#print(QR)
# scan = admin.analizarQRCamara()
# if scan == 'ErrorCode:01-No hay camara':
# scan = admin.analizarQRImagen('prueba.png')
# print(scan)