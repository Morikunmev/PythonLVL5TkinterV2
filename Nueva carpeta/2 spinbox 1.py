import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.label1 = ttk.Label(self.ventana1,text="Seleccione la cantidad de bultos: ")
        self.label1.grid(column=0,row=0,padx=10,pady=10)

        self.spinbox1 = ttk.Spinbox(self.ventana1,increment=3,from_=1,to=10,state="readonly")
        dias = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
        self.spinbox1 = ttk.Spinbox(self.ventana1,values=dias,state="readonly")
        self.spinbox1.set(dias[0])

aplicacion1 = Aplicacion()