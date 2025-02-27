import tkinter as tk
import random
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.canvas1 = tk.Canvas(self.ventana1,width=900,height=500,background="black")
        self.canvas1.grid(column=0,row=0)

        for x in range(101):
            x1 = random.randint(1,900)
            y1 = random.randint(1,500)
            self.cuadrado = self.canvas1.create_rectangle(x1,y1,x1+20,y1+20,fill="red",outline="red",tags="movil")

        self.canvas1.tag_bind("movil","<ButtonPress-1>",self.presion_boton)
        self.canvas1.tag_bind("movil","<Button1-Motion>",self.mover)
        self.cuadrado_seleccionado = None
        self.ventana1.mainloop()
    def presion_boton(self,evento):
        cuadrado = self.canvas1.find_withtag(tk.CURRENT)
        self.cuadrado_seleccionado = (cuadrado,evento.x,evento.y)
    def mover(self,evento):
        x,y = evento.x,evento.y
        cuadrado,x1,y1 = self.cuadrado_seleccionado
        self.canvas1.move(cuadrado,x-x1,y-y1)
        self.cuadrado_seleccionado=(cuadrado,x,y)
aplicacion1 = Aplicacion()
