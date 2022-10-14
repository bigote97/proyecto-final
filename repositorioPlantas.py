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
  
  def guardarPlantas(self, plantas):
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
    siembra_temp = datos_planta[3].split("-")
    cosecha_temp = datos_planta[4].split("-")
    siembra = datetime.date(int(siembra_temp[0]),int(siembra_temp[1]),int(siembra_temp[2]))
    cosecha = datetime.date(int(cosecha_temp[0]),int(cosecha_temp[1]),int(cosecha_temp[2]))
    planta = Planta(datos_planta[0], datos_planta[1], datos_planta[2], siembra, cosecha)
    return planta

  def planta_a_fila(self, planta):
    fecha_cosecha = planta.cosecha
    fecha_siembra = planta.siembra
    fecha_siembra_text = str(fecha_siembra.year)+"-"+str(fecha_siembra.month)+"-"+str(fecha_siembra.day)
    fecha_cosecha_text = str(fecha_cosecha.year)+"-"+str(fecha_cosecha.month)+"-"+str(fecha_cosecha.day)

    return planta.id + "," + planta.nombre + "," + planta.tipo + "," + fecha_siembra_text + "," + fecha_cosecha_text
