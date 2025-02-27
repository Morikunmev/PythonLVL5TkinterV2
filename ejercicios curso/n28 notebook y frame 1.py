import tkinter as tk
from tkinter import ttk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Prueba del control Notebook")

        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Button")
        self.label1 = ttk.Label(self.pagina1,text="La clase Button nos permite capturar el click")
        self.label1.grid(column=0,row=0)
        self.button1 = ttk.Button(self.pagina1,text="Ejemplo de boton")
        self.button1.grid(column=0,row=1)
        self.button2 = ttk.Button(self.pagina1,text="Ejemplo de boton inactivo",state="disabled")
        self.button2.grid(column=0,row=2)

        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Label")
        self.label2 = ttk.Label(self.pagina2,text="La clase label permite mostrar un mensaje")
        self.label2.grid(column=0,row=0)
        self.label3 = ttk.Label(self.pagina2,text="Con los caracteres alalalala")
        self.label3.grid(column=0,row=1)

        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="Entry")
        self.label4 = ttk.Label(self.pagina3,text="En tkinter el control de entrada de datos es nose")
        self.label4.grid(column=0,row=0)
        self.entrada1 = ttk.Entry(self.pagina3,width=30)
        self.entrada1.grid(column=0,row=1)

        self.cuaderno1.grid(column=0,row=0)

        self.ventana1.mainloop()
aplicacion1 = Aplicacion()
















