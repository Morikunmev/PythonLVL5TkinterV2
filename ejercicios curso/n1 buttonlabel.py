import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana = tk.Tk()
        self.ventana.title("Controles Button y Label")

        self.label1 = tk.Label(self.ventana,text=self.valor)
        self.label1.grid(column =0,row=0)
        self.label1.configure(background="red")

        self.boton1 = tk.Button(self.ventana,text="Incrementar",command=self.incrementar)
        self.boton1.grid(column=0,row =1)

        self.boton2 = tk.Button(self.ventana,text="Decrementar",command=self.decrementar)
        self.boton2.grid(column=0,row=2)

        self.ventana.mainloop()
    def incrementar(self):
        self.valor = self.valor +1
        self.label1.configure(text=self.valor)
    def decrementar(self):
        self.valor = self.valor -1
        self.label1.configure(text=self.valor)
aplicacion1 = Aplicacion()

















