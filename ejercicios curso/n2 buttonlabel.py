import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio")

        self.label1 = tk.Label(self.ventana,text="Sistemas de facturacion")
        self.label1.grid(column=0,row=0)

        self.label2 = tk.Label(self.ventana,text="2020")
        self.label2.grid(column=0,row=1)

        self.boton1 = tk.Button(self.ventana,text="Finalizar",command=self.finalizar)
        self.boton1.grid(column=0,row=2)
        self.ventana.resizable(False,False)
        self.ventana.mainloop()
    def finalizar(self):
        sys.exit(0)
aplicacion1 = Aplicacion()


















