import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana,text="Ingrese el nombre de usuario: ")
        self.label1.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=20,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.boton1 = tk.Button(self.ventana,text="Ingresar",command=self.ingresar)
        self.boton1.grid(column=1,row=1)

        self.ventana.mainloop()
    def ingresar(self):
        self.ventana.title(self.dato1.get())

aplicacion1 = Aplicacion()