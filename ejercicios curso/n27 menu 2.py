import tkinter as tk
from tkinter import ttk
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)

        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Cambiar dimension de ventana",command=self.fijartamaño)
        opciones1.add_command(label="Finalizar Programa",command=self.finalizar)
        menubar1.add_cascade(label="Opciones",menu=opciones1)

        self.label1 = ttk.Label(self.ventana1,text="Ingrese el ancho de la ventan")
        self.label1.grid(column=0,row=0)

        self.ancho = tk.StringVar()
        self.entrada1 = ttk.Entry(self.ventana1,width=10,textvariable=self.ancho)
        self.entrada1.grid(column=0,row=1)

        self.label2 = ttk.Label(self.ventana1,text="Ingrese el alto de la ventana")
        self.label2.grid(column=0,row=2)

        self.alto = tk.StringVar()
        self.entrada2 = ttk.Entry(self.ventana1,width=10,textvariable=self.alto)
        self.entrada2.grid(column=0,row=3)

        self.ventana1.mainloop()
    def fijartamaño(self):
        self.ventana1.geometry(self.ancho.get() + "x" + self.alto.get())
    def finalizar(self):
        sys.exit(0)
aplicacion1 = Aplicacion()










