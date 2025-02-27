import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba del control Entry")

        self.label1 = tk.Label(self.ventana,text="Ingrese un numero: ")
        self.label1.grid(column=0,row=0)

        self.dato1=tk.StringVar()
        self.entry1 = tk.Entry(self.ventana,width=10,textvariable=self.dato1)
        self.entry1.grid(column=0,row=1)

        self.boton1 = tk.Button(self.ventana,text="Calcular cuadrado",command=self.calcularcuadrado)
        self.boton1.grid(column=0,row=2)

        self.label2 = tk.Label(self.ventana,text="Resultado")
        self.label2.grid(column=0,row=3)

        self.ventana.mainloop()
    def calcularcuadrado(self):
        valor = int(self.dato1.get())
        cuadrado = valor*valor
        self.label2.configure(text=cuadrado)
aplicacion1 = Aplicacion()