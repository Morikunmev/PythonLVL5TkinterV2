import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana,text="Ingrese primer valor: ")
        self.label1.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=20,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.label2 = tk.Label(self.ventana,text="Ingrese segundo valor: ")
        self.label2.grid(column=0,row=1)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=20,textvariable=self.dato2)
        self.entrada2.grid(column=1,row=1)

        self.boton1 = tk.Button(self.ventana,text="Sumar",command=self.sumar)
        self.boton1.grid(column=1,row=2)

        self.label3 = tk.Label(self.ventana,text="Resultado")
        self.label3.grid(column=1,row=3)

        self.ventana.mainloop()
    def sumar(self):
        suma = int(self.dato1.get()) + int(self.dato2.get())
        self.label3.configure(text=suma)
aplicacion1 = Aplicacion()





















