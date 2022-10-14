# Modelado de cada planta
import datetime

class Planta:
  def __init__(self, id, nombre, tipo, siembra, cosecha):
    self.id = id
    self.nombre = nombre
    self.tipo = tipo
    self.siembra = siembra
    self.cosecha = cosecha
  
  def existePlanta(self, busqueda):
    return ((busqueda in self.nombre) or (busqueda in self.tipo))

  def existeID(self, Id):
    return Id in self.id