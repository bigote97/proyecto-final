# Desde aqui se administraran todas las acciones respecto a las plantas:
# Buscar, agregar, modificar, eliminar

from numpy import true_divide
from planta import Planta
from repositorioPlantas import Repositorio

class Administrador:
  def __init__(self, listado_plantas = []):
    self.repositorio = Repositorio()
    self.plantas = self.repositorio.obtener_plantas()
  
  def agregar_planta(self, id, planta, tipo, siembra, cosecha):
    planta = Planta(id, planta, tipo, siembra, cosecha)
    self.plantas.append(planta)
    return planta

  def buscar_texto(self, filtro):
    return [ planta for planta in self.plantas if planta.coincide(filtro) ]

  def _buscar_por_id(self, id_planta):
    for planta in self.plantas:
      if str(planta.id) == str(id_planta):
        return planta
    return None

  def eliminar_planta(self, id_planta):
    planta = self._buscar_por_id(id_planta)
    if planta:
      self.plantas.remove(planta)
      Repositorio.guardar_plantas(self.plantas)
      return True
    return False