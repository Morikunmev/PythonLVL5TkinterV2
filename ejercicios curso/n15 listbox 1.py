import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.lisbox1 = tk.Listbox(self.ventana)
        self.lisbox1.grid(column=0,row=0)
        self.lisbox1.insert(0,"papas")
        self.lisbox1.insert(1,"manzanas")
        self.lisbox1.insert(2,"melon")
        self.lisbox1.insert(3,"naranjas")
        self.lisbox1.insert(4,"uvas")
        self.lisbox1.insert(5,"cerezas")

        self.boton1 = tk.Button(self.ventana,text="Recupear",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.label1 = tk.Label(self.ventana,text="Seleccionado: ")
        self.label1.grid(column=0,row=2)

        self.ventana.mainloop()
    def recuperar(self):
        if len(self.lisbox1.curselection())!=0:
            self.label1.configure(text=self.lisbox1.get(self.lisbox1.curselection()[0]))
aplicacion1 = Aplicacion()













