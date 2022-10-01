# Manejador de base de datos, en este caso utilizaremos un archivo de texto
import datetime
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
        fila_por_planta = self.nota_a_texto(planta)
        file_path.write(fila_por_planta)
      print("Guardado en "+ self.archivo)

  def agregar_planta(self):
    pass

  def fila_a_planta(self, fila):
    texto = fila[:-1] # Elimina el ultimo caracter, en este caso el salto de linea
    datos_planta = fila.split(',')
    planta = print('Planta: ' + datos_planta[0] + ', tipo: ' + datos_planta[1] + ', sembrada: ' + datos_planta[2] + ', cosechar: ' + datos_planta[3])
    return planta

  def planta_a_fila(self, planta):
    pass

archivo = Repositorio()
archivo.obtener_plantas()