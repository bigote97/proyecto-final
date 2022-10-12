# Interfaz grafica del programa
import tkinter
from tkinter import ttk

class Gui():
  def __init__(self):
    self.iniciar_gui()
  def finalizarPrograma(self):
    self.repositorio.guardar_todo(self.anotador.notas)
    self.ventana_principal.destroy()
  def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Anotador")
        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar nota", 
                          command = self.agregar_nota).grid(row=0, column=0)
        botonModificar=tkinter.Button(self.ventana_principal,text="Modificar",
                          command = self.modificar_nota).grid(row=0, column=1)
        botonEliminar=tkinter.Button(self.ventana_principal, text = "Eliminar",
                          command = self.eliminar_nota).grid(row=0, column=2)
        tkinter.Label(self.ventana_principal,text="Buscar").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar",
                          command = self.buscar_notas).grid(row=1, column=2)
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal, 
                                    columns=("texto", "etiquetas"))
        self.treeview.heading("#0", text="id")
        self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("texto", text="Texto")
        self.treeview.heading("etiquetas", text="Etiquetas")
        self.treeview.grid(row=10, columnspan=3)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()
if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()