# Interfaz grafica del programa
from operator import iadd
from platform import platform
from re import I, T
import tkinter
from tkinter import ttk

from cv2 import validateDisparity
from repositorioPlantas import Repositorio
from administracion import Administrador
class Gui():
  def __init__(self):
    self.iniciarAdministracion()
    self.iniciar_gui()

  def finalizarPrograma(self):
    self.repositorio.guardar_todo(self.anotador.notas)
    self.ventana_principal.destroy()

  def iniciarGui(self):

      self.ventana_principal = tkinter.Tk()
      self.ventana_principal.title("Administración de Plantas")
      botonAgregar = tkinter.Button(self.ventana_principal, text="Agregar planta",
                                    command=self.agregar_nota).grid(row=0, column=0)
      botonModificar = tkinter.Button(self.ventana_principal, text="Modificar",
                                      command=self.modificar_nota).grid(row=0, column=1)
      botonEliminar = tkinter.Button(self.ventana_principal, text="Eliminar",
                                     command=self.eliminar_nota).grid(row=0, column=2)
      tkinter.Label(self.ventana_principal,
                    text="Buscar").grid(row=1, column=0)
      self.cajaBuscar = tkinter.Entry(self.ventana_principal)
      self.cajaBuscar.grid(row=1, column=1)
      botonBuscar = tkinter.Button(self.ventana_principal, text="Buscar",
                                   command=self.buscar_notas).grid(row=1, column=2)
      self.treeview = ttk.Treeview(self.ventana_principal)
      self.treeview = ttk.Treeview(self.ventana_principal,
                                   columns=("Nombre", "Tipo"))
      self.treeview.heading("#0", text="id")
      self.treeview.column("#0", minwidth=0, width="40")
      self.treeview.heading("Nombre", text="Nombre")
      self.treeview.heading("Tipo", text="Tipo")
      self.treeview.grid(row=10, columnspan=3)
      self.cargarPlantas()
      botonSalir = tkinter.Button(self.ventana_principal, text="Salir",
                                  command=self.salir).grid(row=11, column=1)
      self.cajaBuscar.focus()

  def iniciarAdministracion(self):
    repositorio = Repositorio()
    listaPlantas = Repositorio.obtener_plantas()
    self.administrador = Administrador(listaPlantas)

  def cargarPlantas(self, plantas=None):
    for i in self.treeview.get_children():
      self.treeview.delete(i)
    if not plantas:
      plantas = self.administrador.plantas
    for planta in plantas:
      item = self.treeview.insert("", tkinter.END, text=planta.id, values=(
          planta.nombre, planta.tipo), iid=planta.id)

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
    botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                            command=self.agregar_ok)
    self.modalAgregar.bind("<Return>", self.agregar_ok)
    botonOK.grid(row=2)
    botonCancelar = tkinter.Button(self.modalAgregar, text="Cancelar",
                                  command=self.modalAgregar.destroy)
    botonCancelar.grid(row=2, column=2)

  def confirmarPlanta(self, event=None):
    planta = self.administrador.agregarPlanta(
        self.planta.get(), self.tipo.get())
    self.modalAgregar.destroy()
    item = self.treeview.insert("", tkinter.END, text=planta.id, values=(
        planta.nombre, planta.tipo), iid=planta.id)


if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
