import tkinter as tk
from tkinter import ttk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.listbox1 = tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papas")
        self.listbox1.insert(1,"Manzanas")
        self.listbox1.insert(2,"sandia")
        self.listbox1.insert(3,"naranja")
        self.listbox1.insert(4,"pera")
        self.listbox1.insert(5,"melon")

        self.boton1 = ttk.Button(self.ventana1,text="Recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.label1 = ttk.Label(self.ventana1,text="Seleccionado")
        self.label1.grid(column=0,row=2)

        self.ventana1.mainloop()
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))
aplicacion1 = Aplicacion()