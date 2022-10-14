# Modelado de cada planta
import datetime

class Planta:
  def __init__(self, id, planta, tipo, siembra=datetime.date.today(), cosecha=datetime.date.today()):
    self.nombre = planta
    self.tipo = tipo
    self.siembra = siembra
    self.cosecha = cosecha
    self.id = id
  
  def existePlanta(self, busqueda):
    return ((busqueda in self.nombre) or (busqueda in self.tipo))

  def existeID(self, Id):
    return Id in self.id