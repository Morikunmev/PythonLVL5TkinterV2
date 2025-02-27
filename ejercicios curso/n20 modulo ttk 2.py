import tkinter as tk
from tkinter import ttk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.label1 = ttk.Label(self.ventana,text="Ingrese nombre de usuario: ")
        self.label1.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entry1.grid(column=1,row=0)

        self.label2 = ttk.Label(self.ventana,text="Ingrese clave: ")
        self.label2.grid(column=0,row=1)

        self.dato2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.ventana,width=30,textvariable=self.dato2)
        self.entry2.grid(column=1,row=1)

        self.boton1 = ttk.Button(self.ventana,text="Ingresar",command=self.ingresar)
        self.boton1.grid(column=1,row=2)

        self.ventana.mainloop()
    def ingresar(self):
        if self.dato2.get() == "Juan" and self.dato2.get() == "abc123":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")
aplicacion1 = Aplicacion()