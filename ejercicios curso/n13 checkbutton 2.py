import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana,text="Esta de acuerdo con los terminos y condiciones?",
                                     variable=self.seleccion,command=self.cambiarestado)
        self.check1.grid(column=0,row=0)

        self.boton1 = tk.Button(self.ventana,text="Entrar",state="disabled",command=self.ingresar)
        self.boton1.grid(column=0,row=1)

        self.ventana.mainloop()
    def cambiarestado(self):
        if self.seleccion.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion.get()==0:
            self.boton1.configure(state="disabled")
    def ingresar(self):
        self.ventana.title("Ingresando...")

cancion1 = Aplicacion()























