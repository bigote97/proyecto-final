# Desde aqui se administraran todas las acciones respecto a las plantas:
# Buscar, agregar, modificar, eliminar

from datetime import date
from planta import Planta
from repositorioPlantas import Repositorio


class Administrador:
  def __init__(self, listado_plantas = []):
    #self.repositorio = Repositorio()
    self.plantas = listado_plantas
  
  def agregarPlanta(self, planta, tipo, siembra = "otra", cosecha = "otro"):
    tamanio_lista = len(self.plantas) - 1
    ultimo_id = self.plantas[tamanio_lista].id
    id = str(int(ultimo_id) + 1)

    planta = Planta(id, planta, tipo, siembra, siembra, '0')
    self.plantas.append(planta)
    repo = Repositorio()
    repo.agregar_planta(planta)
    return planta

  def buscarxTexto(self, filtro):
    repo = Repositorio()
    encontradas = repo.buscar_nombre_plantas(filtro)
    return encontradas

  def buscarID(self, id_planta):
    repo = Repositorio()
    encontradas = repo.buscar_planta_id(id_planta)
    return encontradas

  def eliminarPlanta(self, id_planta):
    planta = self.buscarID(id_planta)
    if planta:
      planta.baja = '1'
      repo = Repositorio()
      repo.eliminar_planta(planta)
      return True
    return False

  def modificarPlanta(self, id_planta, fec_cosecha, tipo):
    planta = self.buscarID(id_planta)
    if planta:
      planta.tipo = tipo
      cosecha_temp = fec_cosecha.split("-")
      planta.cosecha = date(int(float(cosecha_temp[0])),int(float(cosecha_temp[1])),int(float(cosecha_temp[2])))
      repo = Repositorio()
      repo.modificar_planta(planta)
      return True
    return False

  def cargarTipos(self):
    lista_tipos=[]
    # cambiar a set
    for planta in self.plantas:
      if planta.baja == '0':
        if not planta.tipo in lista_tipos:
          lista_tipos.append(planta.tipo)
    return lista_tipos
    