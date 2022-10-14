# Manejador de base de datos, en este caso utilizaremos un archivo de texto
import datetime
from planta import Planta
class Repositorio:
  def __init__(self, archivo = "plantas.txt"):
    self.archivo = archivo

  def obtener_plantas(self):
    plantas = []
    with open(self.archivo, 'r') as file_path:
      for fila in file_path:
        n = self.fila_a_planta(fila)
        plantas.append(n)
    return plantas
  
  def guardar_plantas(self, plantas):
    with open(self.archivo, 'w') as file_path:
      for planta in plantas:
        fila_por_planta = self.planta_a_fila(planta)
        file_path.write(fila_por_planta)
      print("Guardado en "+ self.archivo)

  def agregar_planta(self):
    pass

  def fila_a_planta(self, fila):
    fila = fila[:-1] # Elimina el ultimo caracter, en este caso el salto de linea
    datos_planta = fila.split(',')
    planta = Planta(38,datos_planta[0], datos_planta[1], datos_planta[2], datos_planta[3])
    return planta

  def planta_a_fila(self, planta):
    return planta.id + "," + planta.nombre + "," + planta.tipo + "," + planta.siembra + "," + planta.cosecha