# Modelado de cada planta
import datetime

class Planta:
  def __init__(self, id, nombre, tipo, siembra, cosecha, baja):
    self.id = id
    self.nombre = nombre
    self.tipo = tipo
    self.siembra = siembra
    self.cosecha = cosecha
    self.baja = baja
  
  def existePlanta(self, busqueda):
    return ((busqueda in self.nombre) or (busqueda in self.tipo))

  def existeID(self, Id):
    return Id in self.id