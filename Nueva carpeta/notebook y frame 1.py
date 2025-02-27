import tkinter as tk
from tkinter import ttk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Prueba del control de Notebook")

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cuaderno1.grid(column=0,row=0)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Button")

        self.texto1 = ttk.Label(self.pagina1,text="Xd")
        self.texto1.grid(column=0,row=0)
        self.boton1 = ttk.Button(self.pagina1,text="Ejemplo de boton")
        self.boton1.grid(column=0,row=1)

        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Label")
        self.texto2 = ttk.Label(self.pagina2,text="XdSSS")
        self.texto2.grid(column=0,row=0)

        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="Entry")
        self.texto3 = ttk.Label(self.pagina3,text="En tkinter el control de que nose que")
        self.texto3.grid(column=0,row=0)

        self.ventana1.mainloop()
aplicacion1 = Aplicacion()


