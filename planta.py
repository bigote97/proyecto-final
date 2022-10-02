# Modelado de cada planta
import datetime

class Planta:
  def __init__(self, id, planta, tipo, siembra=datetime.date.today(), cosecha=datetime.date.today()):
    self.planta = planta
    self.tipo = tipo
    self.siembra = siembra
    self.cosecha = cosecha
    self.id = id
  
  def existe_planta(self, busqueda):
    return ((busqueda in self.planta) or (busqueda in self.tipo))

  def existe_id(self, Id):
    return Id in self.id