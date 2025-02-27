import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.canvas1 = tk.Canvas(self.ventana1,width=777,height=777)
        self.canvas1.grid(column=0,row=0)
        self.canvas1.create_rectangle(8,60,70,8,fill="white")

        self.ventana1.mainloop()
aplicacion1 = Aplicacion()