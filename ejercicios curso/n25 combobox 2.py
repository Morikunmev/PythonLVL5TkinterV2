import tkinter as tk
from tkinter import ttk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = ttk.Label(self.ventana,text = "Ingrese nombre")
        self.label1.grid(column=0,row=0)

        self.nombre = tk.StringVar()
        self.entrada1 = ttk.Entry(self.ventana,width=40,textvariable=self.nombre)
        self.entrada1.grid(column=0,row=1)

        self.label2 = ttk.Label(self.ventana,text="Selecciones pais")
        self.label2.grid(column=0,row=2)

        self.pais = tk.StringVar()
        paises = ("Chile","Argentina","Uruguay","Mexico","Colombia")
        self.combobox1 = ttk.Combobox(self.ventana,width=10,textvariable=self.pais,values=paises,state="readonly")
        self.combobox1.grid(column=0,row=3)
        self.combobox1.current(0)

        self.boton1 = ttk.Button(self.ventana,text="Recuperar",command=self.mostrardatos)
        self.boton1.grid(column=0,row=4)

        self.ventana.mainloop()
    def mostrardatos(self):
        self.ventana.title("Nombre: " + self.nombre.get() + " Pais: " +self.combobox1.get())
aplicacion1 = Aplicacion()

















