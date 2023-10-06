# Manejador de base de datos, en este caso utilizaremos un archivo de texto
import datetime
from planta import Planta

from credentials import getCredentials
import mysql.connector

class Repositorio:
  def __init__(self):
    self.bd = mysql.connector.connect(**getCredentials())
    self.cursor = None
    if self.bd and self.bd.is_connected:
        self.cursor = self.bd.cursor()

  def obtener_plantas(self):
    plantas = []
    query = "SELECT id, name, type, planting, harvest, baja FROM plants"
    self.cursor.execute(query)
    response = self.cursor.fetchall()
    for id, name, type, planting, harvest, baja in response:
      plantingDia = planting.day
      plantingMes = planting.month
      plantingAnio = planting.year
      siembra = datetime.date(plantingAnio, plantingMes, plantingDia)
      harvestDia = harvest.day
      harvestMes = harvest.month
      harvestAnio = harvest.year
      cosecha = datetime.date(harvestAnio, harvestMes, harvestDia)
      p = Planta(id, name, type, siembra, cosecha, baja)
      plantas.append(p)
    return plantas

  def buscar_nombre_plantas(self, text):
    plantas = []
    query = "SELECT id, name, type, planting, harvest, baja FROM plants"
    query += " WHERE name LIKE %s"
    values = [
      '%'+ text +'%'
    ]
    self.cursor.execute(query, values)
    response = self.cursor.fetchall()
    for id, name, type, planting, harvest, baja in response:
      plantingDia = planting.day
      plantingMes = planting.month
      plantingAnio = planting.year
      siembra = datetime.date(plantingAnio, plantingMes, plantingDia)
      harvestDia = harvest.day
      harvestMes = harvest.month
      harvestAnio = harvest.year
      cosecha = datetime.date(harvestAnio, harvestMes, harvestDia)
      p = Planta(id, name, type, siembra, cosecha, baja)
      plantas.append(p)
    return plantas

  def buscar_planta_id(self, ID):
    plantas = []
    query = "SELECT id, name, type, planting, harvest, baja FROM plants"
    query += " WHERE id = %s"
    values = [
      ID,
    ]
    self.cursor.execute(query, values)
    response = self.cursor.fetchall()
    for id, name, type, planting, harvest, baja in response:
      plantingDia = planting.day
      plantingMes = planting.month
      plantingAnio = planting.year
      siembra = datetime.date(plantingAnio, plantingMes, plantingDia)
      harvestDia = harvest.day
      harvestMes = harvest.month
      harvestAnio = harvest.year
      cosecha = datetime.date(harvestAnio, harvestMes, harvestDia)
      p = Planta(id, name, type, siembra, cosecha, baja)
      plantas.append(p)
    return plantas
  
  def agregar_planta(self, planta):
    query = "INSERT INTO plants (name, type, planting, harvest, baja)"
    query += "VALUES (%s, %s, %s, %s, %s)"
    values = [
        planta.nombre,
        planta.tipo,
        planta.siembra,
        planta.cosecha,
        planta.baja
    ]

    try:
      self.cursor.execute(query, values)
      self.bd.commit()
      print("Consulta ejecutada correctamente.")
    except mysql.connector.Error as err:
      print(f"Error al ejecutar la consulta: {err}")

  def modificar_planta(self, planta):
    query = "UPDATE plants "
    query += "SET type = %s, harvest =%s "
    query += "WHERE id = %s"
    values = [
        planta.tipo,
        planta.cosecha,
        planta.id,
    ]

    try:
      self.cursor.execute(query, values)
      self.bd.commit()
      print("Consulta ejecutada correctamente.")
    except mysql.connector.Error as err:
      print(f"Error al ejecutar la consulta: {err}")

  def eliminar_planta(self, planta):
    query = "UPDATE plants "
    query += "SET baja = %s "
    query += "WHERE id = %s"
    values = [
        '1',
        planta.id
    ]

    try:
      self.cursor.execute(query, values)
      self.bd.commit()
      print("Consulta ejecutada correctamente.")
    except mysql.connector.Error as err:
      print(f"Error al ejecutar la consulta: {err}")