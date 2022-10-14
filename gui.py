# Interfaz grafica del programa
from datetime import date, datetime
from dis import show_code
from email import message
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import COLUMN, Tree

from cv2 import validateDisparity
from pkg_resources import working_set
from planta import Planta
from repositorioPlantas import Repositorio
from administracion import Administrador
from funcionesQR import qrReader
from funcionesQR import qrReaderFile
from funcionesQR import qrGenerator

class Gui():
  def __init__(self):
    self.iniciarAdministracion()
    self.iniciarGui()

  def iniciarGui(self):

      self.ventana_principal = tkinter.Tk()
      self.ventana_principal.title("Administración de Plantas")
      botonAgregar = tkinter.Button(self.ventana_principal, text="Agregar planta",
                                    command=self.agregarPlantas).grid(row=0, column=0)
      botonModificar = tkinter.Button(self.ventana_principal, text="Modificar",
                                      command=self.modificarPlanta).grid(row=0, column=1)
      botonEliminar = tkinter.Button(self.ventana_principal, text="Eliminar",
                                    command=self.eliminarPlanta).grid(row=0, column=2)
      tkinter.Label(self.ventana_principal,
                    text="Buscar").grid(row=1, column=0)
      self.cajaBuscar = tkinter.Entry(self.ventana_principal)
      self.cajaBuscar.grid(row=1, column=1)
      botonBuscar = tkinter.Button(self.ventana_principal, text="Buscar",
                                  command=self.buscarPlanta).grid(row=1, column=2)
      botonBuscarQR = tkinter.Button(self.ventana_principal, text="Buscar QR",
                                  command=self.buscarPlantaQR).grid(row=1, column=3)
      self.treeview = ttk.Treeview(self.ventana_principal)
      self.treeview = ttk.Treeview(self.ventana_principal,
                                  columns=("Nombre", "Tipo","Siembra","Cosecha"))
      self.treeview.heading("#0", text="id")
      self.treeview.column("#0", minwidth=0, width="40")
      self.treeview.heading("Nombre", text="Nombre")
      self.treeview.heading("Tipo", text="Tipo")
      self.treeview.heading("Siembra", text="Siembra")
      self.treeview.heading("Cosecha", text="Cosecha")
      self.treeview.grid(row=10, columnspan=3)
      self.cargarPlantas()
      botonSalir = tkinter.Button(self.ventana_principal, text="Salir",
                                  command=self.salirPrograma).grid(row=11, column=1)
      self.cajaBuscar.focus()

  def iniciarAdministracion(self):
    repositorio = Repositorio()
    listaPlantas = repositorio.obtener_plantas()
    self.administrador = Administrador(listaPlantas)
    tipos = self.administrador.cargarTipos()
    print(tipos)

  def cargarPlantas(self, plantas=None):
    for i in self.treeview.get_children():
      self.treeview.delete(i)
    if not plantas:
      plantas = self.administrador.plantas
    for planta in plantas:
      item = self.treeview.insert("", tkinter.END, text=planta.id, values=(
          planta.nombre, planta.tipo, planta.siembra, planta.cosecha), iid=planta.id)

  def agregarPlantas(self):
    self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
    #top.transient(parent)
    self.modalAgregar.grab_set()
    tkinter.Label(self.modalAgregar, text="ID: ").grid(row=0,column=0)
    self.ID = tkinter.Entry(self.modalAgregar)
    self.ID.grid(row=0,column=1,columnspan=2)
    tkinter.Label(self.modalAgregar, text="Planta: ").grid(row=1, column=0)
    self.nombre = tkinter.Entry(self.modalAgregar)
    self.nombre.grid(row=1, column=1, columnspan=2)
    self.nombre.focus()
    tkinter.Label(self.modalAgregar, text="Tipo: ").grid(row=3)
    self.tipo = tkinter.Entry(self.modalAgregar)
    self.tipo.grid(row=3, column=1, columnspan=2)
    botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                            command=self.confirmarPlanta)
    self.modalAgregar.bind("<Return>", self.confirmarPlanta)
    botonOK.grid(row=4)
    botonCancelar = tkinter.Button(self.modalAgregar, text="Cancelar",
                                  command=self.modalAgregar.destroy)
    botonCancelar.grid(row=4, column=2)

  def confirmarPlanta(self, event=None):
    planta = self.administrador.agregarPlanta(self.ID.get(), self.nombre.get(), self.tipo.get(), date.today(),date.today())
    self.modalAgregar.destroy()
    item = self.treeview.insert("", tkinter.END, text=planta.id, values=(
        planta.nombre, planta.tipo,planta.siembra,planta.cosecha), iid=planta.id)

  def modificarPlanta(self):
    if not self.treeview.selection():
      messagebox.showwarning("Sin selección","Seleccione primero la nota a modificar")
      return False
    item = self.treeview.selection()
    id = self.treeview.item(item)['text']
    planta = self.administrador.buscarID(id)
    print(planta.nombre)

    self.modalModificar = tkinter.Toplevel(self.ventana_principal)
    #top.transient(parent)
    self.modalModificar.grab_set()
    tkinter.Label(self.modalModificar, text="ID: ").grid(row=0,column=0)
    tkinter.Label(self.modalModificar, text='planta.id').grid(row=0,column=1)
    self.ID.grid(row=0,column=1,columnspan=2)
    tkinter.Label(self.modalModificar, text="Planta: ").grid(row=1, column=0)
    tkinter.Label(self.modalModificar, text=planta.nombre).grid(row=1, column=1)
    self.nombre.grid(row=1, column=1, columnspan=2)
    tkinter.Label(self.modalModificar, text="Tipo: ").grid(row=3)
    self.tipo.focus()
    self.tipo = tkinter.Entry(self.modalModificar)
    self.tipo.grid(row=3, column=1, columnspan=2)
    botonOK = tkinter.Button(self.modalModificar, text="Guardar",
                            command=self.confirmaModificacion)
    self.modalModificar.bind("<Return>", self.confirmaModificacion)
    botonOK.grid(row=4)
    botonCancelar = tkinter.Button(self.modalModificar, text="Cancelar",
                                  command=self.modalModificar.destroy)
    botonCancelar.grid(row=4, column=2)

  def confirmaModificacion(self, event=None):
    item = self.treeview.selection()
    id = self.treeview.item(item)['text']
    planta = self.administrador.buscarID(id) 

    self.administrador.modificarPlanta(id, self.tipo.get(), planta.cosecha)

    self.treeview.set()

    self.modalModificar.destroy(self.treeview.selection()[0], column='tipo', value=self.tipo.get())

  def eliminarPlanta(self):
    if not self.treeview.selection():
      messagebox.showwarning("Sin selección","Seleccione primero la nota a modificar")
      return False
    item = self.treeview.selection()
    id = self.treeview.item(item)['text']
    planta = self.administrador.buscarID(id)
    if planta:
      if self.administrador.eliminarPlanta(id):
        self.treeview.delete(id)
      else:
        messagebox.showwarning("Error al eliminar","Hubo un error vuelva a intentar")
    print(planta.nombre)

  def buscarPlanta(self):
    filtro = self.cajaBuscar.get()
    plantas = self.administrador.buscarxTexto(filtro)
    if plantas:
      self.cargarPlantas(plantas)
    else:
      messagebox.showwarning("Sin resultados", "Ninguna nota coincide con la búsqueda")

  def buscarPlantaQR(self):
    scan = self.analizarQRCamara
    if scan == 'ErrorCode:01-No hay camara':
      scan = self.analizarQRImagen('prueba.png')
    print(scan)

  def analizarQRCamara(self):
    scan = qrReader.scanQRCode()
    if scan == 'ErrorCode:01-No hay camara':
      scan = qrReaderFile.readQRCode('prueba.png')
    return scan
  
  def analizarQRImagen(self, ruta):
    scan = qrReaderFile.readQRCode(ruta)
    return scan
 

  def generarQR(self, nombre, id):
    QR = qrGenerator.generadorQR(nombre, id)
    return QR

  def salirPrograma(self):
    repo = Repositorio()
    repo.guardarPlantas(self.administrador.plantas)
    self.ventana_principal.destroy()


if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
