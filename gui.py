# Interfaz grafica del programa
from datetime import date
import datetime
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import COLUMN, Tree

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
      botonAgregar = tkinter.Button(self.ventana_principal, text="Agregar planta", command=self.agregarPlantas).grid(row=0, column=0)
      botonModificar = tkinter.Button(self.ventana_principal, text="Modificar", command=self.modificarPlanta).grid(row=0, column=1)
      botonEliminar = tkinter.Button(self.ventana_principal, text="Eliminar", command=self.eliminarPlanta).grid(row=0, column=2)
      botonGenerarQR = tkinter.Button(self.ventana_principal, text="Generar QR", command=self.generarQR).grid(row=0, column=3)
      self.cajaBuscar = tkinter.Entry(self.ventana_principal)
      self.cajaBuscar.grid(row=1, column=0)
      botonBuscar = tkinter.Button(self.ventana_principal, text="Buscar", command=self.buscarPlanta).grid(row=1, column=1)
      tipos = self.administrador.cargarTipos()
      tipo_elegido = tkinter.StringVar(self.ventana_principal)
      tipo_elegido.set(tipos[0]) # default value
      self.buscar_tipo = ttk.OptionMenu(self.ventana_principal, tipo_elegido,"", *tipos, command=self.buscarTipo)
      self.buscar_tipo.grid(row=1, column=2)

      botonBuscarQR = tkinter.Button(self.ventana_principal, text="Buscar QR", command=self.buscarPlantaQR).grid(row=1, column=3)
                                
      self.treeview = ttk.Treeview(self.ventana_principal)
      self.treeview = ttk.Treeview(self.ventana_principal, columns=("Nombre", "Tipo","Siembra","Cosecha"))
      self.treeview.heading("#0", text="id")
      self.treeview.column("#0", minwidth=0, width="40")
      self.treeview.heading("Nombre", text="Nombre")
      self.treeview.heading("Tipo", text="Tipo")
      self.treeview.heading("Siembra", text="Siembra")
      self.treeview.heading("Cosecha", text="Cosecha")
      self.treeview.grid(row=10, columnspan=3)
      self.cargarPlantas()
      botonSalir = tkinter.Button(self.ventana_principal, text="Salir", command=self.salirPrograma).grid(row=11, column=1)
      self.cajaBuscar.focus()

  def iniciarAdministracion(self):
    repositorio = Repositorio()
    listaPlantas = repositorio.obtener_plantas()
    self.administrador = Administrador(listaPlantas)

  def cargarPlantas(self, plantas=None):
    for i in self.treeview.get_children():
      self.treeview.delete(i)
    if not plantas:
      plantas = self.administrador.plantas
    for planta in plantas:
      if planta.baja == '0':
        item = self.treeview.insert("", tkinter.END, text=planta.id, values=(planta.nombre, planta.tipo, planta.siembra, planta.cosecha), iid=planta.id)
      
  def agregarPlantas(self):
    self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
    #top.transient(parent)
    self.modalAgregar.grab_set()
    tkinter.Label(self.modalAgregar, text="Planta: ").grid(row=0, column=0)
    self.nombre = tkinter.Entry(self.modalAgregar)
    self.nombre.grid(row=0, column=1, columnspan=2)
    self.nombre.focus()
    tkinter.Label(self.modalAgregar, text="Tipo: ").grid(row=1)
    self.tipo = tkinter.Entry(self.modalAgregar)
    self.tipo.grid(row=1, column=1, columnspan=2)
    tkinter.Label(self.modalAgregar, text="Cosechar el: ").grid(row=2,column=0)
    self.cosecha = tkinter.Entry(self.modalAgregar)
    self.cosecha.grid(row=2,column=1,columnspan=2)
    botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                            command=self.confirmarPlanta)
    self.modalAgregar.bind("<Return>", self.confirmarPlanta)
    botonOK.grid(row=4)
    botonCancelar = tkinter.Button(self.modalAgregar, text="Cancelar",
                                  command=self.modalAgregar.destroy)
    botonCancelar.grid(row=4, column=2)

  def confirmarPlanta(self, event=None):
    cosecha = self.cosecha.get()
    if cosecha == '':
      cosecha = date.today()
    else:
      cosecha_temp = cosecha.split("-")
      cosecha = datetime.date(int(cosecha_temp[0]),int(cosecha_temp[1]),int(cosecha_temp[2]))
    planta = self.administrador.agregarPlanta(self.nombre.get(), self.tipo.get(), date.today(), cosecha)
    if self.nombre.get() != "":
      self.modalAgregar.destroy()
      item = self.treeview.insert("", tkinter.END, text=planta.id, values=(planta.nombre, planta.tipo,planta.siembra,planta.cosecha), iid=planta.id)
      tipos = self.administrador.cargarTipos()
      self.buscar_tipo.option_clear()
    else:
      messagebox.showwarning("Campos incompletos","Por favor, ingresa los campos correspondientes")

  def modificarPlanta(self):
    if not self.treeview.selection():
      messagebox.showwarning("Sin selección","Seleccione primero la nota a modificar")
      return False
    item = self.treeview.selection()
    id = self.treeview.item(item)['text']
    planta = self.administrador.buscarID(id)
    self.modalModificar = tkinter.Toplevel(self.ventana_principal)
    self.modalModificar.grab_set()
    tkinter.Label(self.modalModificar, text="ID").grid(row=0, column=0)
    tkinter.Label(self.modalModificar, text = "Cosecha: ").grid(row=0, column=0)
    self.cosecha = tkinter.Entry(self.modalModificar)
    self.cosecha.grid(row=0,column=1,columnspan=2)
    self.cosecha.insert(0, planta.cosecha)
    self.cosecha.focus()
    tkinter.Label(self.modalModificar, text = "Tipo: ").grid(row=1)
    self.tipo = tkinter.Entry(self.modalModificar)
    self.tipo.grid(row=1, column=1, columnspan=2)
    self.tipo.insert(0, planta.tipo)
    botonOK = tkinter.Button(self.modalModificar, text="Guardar",
              command=self.confirmarModificacion)
    self.modalModificar.bind("<Return>", self.confirmarModificacion)
    botonOK.grid(row=2)
    botonCancelar = tkinter.Button(self.modalModificar, text = "Cancelar",
              command = self.modalModificar.destroy)
    botonCancelar.grid(row=2,column=2)
  
  def confirmarModificacion(self,event = None):
        item = self.treeview.selection()
        id = self.treeview.item(item)['text']
        nueva_cosecha = self.cosecha.get()
        nuevo_tipo = self.tipo.get()
        print(nueva_cosecha)
        print(nuevo_tipo)
        resultado = self.administrador.modificarPlanta(id, nueva_cosecha, nuevo_tipo)

        if resultado:
            self.treeview.set(self.treeview.selection()[0], column="Cosecha", value=nueva_cosecha)
            self.treeview.set(self.treeview.selection()[0], column="Tipo", value=nuevo_tipo)
            self.modalModificar.destroy()
        else:
            messagebox.showwarning("Error", "Error al modificar la planta")

  def eliminarPlanta(self):
    if not self.treeview.selection():
      messagebox.showwarning(
          "Sin selección", "Seleccione primero la nota a modificar")
      return False
    item = self.treeview.selection()
    id = self.treeview.item(item)['text']
    planta = self.administrador.buscarID(id)
    if planta:
      if self.administrador.eliminarPlanta(id):
        self.treeview.delete(id)
      else:
        messagebox.showwarning(
            "Error al eliminar", "Hubo un error vuelva a intentar mas tarde")
    print(planta.nombre + 'planta eliminada')

  def buscarPlanta(self):
    filtro = self.cajaBuscar.get()
    plantas = self.administrador.buscarxTexto(filtro.lower())
    if plantas:
      self.cargarPlantas(plantas)
    else:
      messagebox.showwarning("Sin resultados", "Ninguna planta coincide con la búsqueda")
  
  def buscarTipo(self, filtro):
    plantas = self.administrador.buscarxTexto(filtro)
    if plantas:
      self.cargarPlantas(plantas)
    else:
      messagebox.showwarning("Sin resultados", "Ninguna planta coincide con la búsqueda")

  def buscarPlantaQR(self):
    scan = qrReader.scanQRCode()
    if not scan == 'ErrorCode:01-No hay camara':
      planta = self.administrador.buscarID(scan)
      if planta:
        self.cargarPlantas([planta])
      else:
        messagebox.showwarning("Sin resultados", "Ninguna planta coincide con la búsqueda")
    else:
      self.modalInputQR()

  def analizarQRImagen(self):
    archivo = self.nombre_archivo.get()
    scan = qrReaderFile.readQRCode(archivo)
    planta = self.administrador.buscarID(scan)
    if planta:
      self.cargarPlantas([planta])
      self.modalArchivoQR.destroy()
    else:
      self.modalArchivoQR.destroy()
      messagebox.showwarning("Sin resultados", "Ninguna planta coincide con la búsqueda")

  def modalInputQR(self):
    self.modalArchivoQR = tkinter.Toplevel(self.ventana_principal)
    self.modalArchivoQR.grab_set()
    tkinter.Label(self.modalArchivoQR, text = "Archivo: ").grid(row=0, column=0)
    self.nombre_archivo = tkinter.Entry(self.modalArchivoQR)
    self.nombre_archivo.grid(row=0,column=1,columnspan=2)
    self.nombre_archivo.focus()
    botonOK = tkinter.Button(self.modalArchivoQR, text="Buscar",
              command=self.analizarQRImagen)
    self.modalArchivoQR.bind("<Return>", self.analizarQRImagen)
    botonOK.grid(row=2)
    botonCancelar = tkinter.Button(self.modalArchivoQR, text = "Cancelar",
              command = self.modalArchivoQR.destroy)
    botonCancelar.grid(row=2,column=2)

  def generarQR(self):
    if not self.treeview.selection():
      messagebox.showwarning("Sin selección","Seleccione primero la nota a modificar")
      return False
    item = self.treeview.selection()
    id = self.treeview.item(item)['text']
    planta = self.administrador.buscarID(id)
    if planta:
      QR = qrGenerator.generadorQR(planta.nombre, planta.id)
      messagebox.showwarning("QR generado con exito!","Imprimi el archivo " + QR + " y pegalo en tu maceta")
    else:
      messagebox.showwarning("Error al crear QR","Hubo un error vuelva a intentar mas tarde")

  def salirPrograma(self):
    self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
