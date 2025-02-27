import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba")

        self.boton1 = tk.Button(self.ventana,text="Varon",command=self.presion_varon)
        self.boton1.grid(column=0,row=0)

        self.boton2 = tk.Button(self.ventana,text="Mujer",command=self.presion_mujer)
        self.boton2.grid(column=0,row=1)

        self.ventana.mainloop()
    def presion_varon(self):
        self.ventana.title("Varon")
    def presion_mujer(self):
        self.ventana.title("Mujer")

aplicacion1 = Aplicacion()


















