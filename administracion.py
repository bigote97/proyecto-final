# Desde aqui se administraran todas las acciones respecto a las plantas:
# Buscar, agregar, modificar, eliminar

from numpy import true_divide
from planta import Planta
from repositorioPlantas import Repositorio

class Administrador:
  def __init__(self, listado_plantas = []):
    self.repositorio = Repositorio()
    self.plantas = self.repositorio.obtener_plantas()
  
  def agregarPlanta(self, id, planta, tipo, siembra, cosecha):
    planta = Planta(id, planta, tipo, siembra, cosecha)
    self.plantas.append(planta)
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
      return True
    return False
