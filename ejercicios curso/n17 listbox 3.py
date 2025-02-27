import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.scrollbar1 = tk.Scrollbar(self.ventana,orient=tk.VERTICAL)
        self.listbox1 = tk.Listbox(self.ventana,selectmode=tk.MULTIPLE,yscrollcommand=self.scrollbar1.set)

        self.listbox1.grid(column=0,row=0)
        self.scrollbar1.configure(command=self.listbox1.yview)
        self.scrollbar1.grid(column=1,row=0,sticky="NS")

        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.listbox1.insert(6,"limon")
        self.listbox1.insert(7,"kiwi")
        self.listbox1.insert(8,"banana")
        self.listbox1.insert(9,"uva")
        self.listbox1.insert(10,"papaya")
        self.listbox1.insert(11,"mandarina")
        self.listbox1.insert(12,"frutilla")

        self.boton1 = tk.Button(self.ventana,text="recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.label1 = tk.Label(self.ventana,text="Seleccionado:")
        self.label1.grid(column=0,row=2)

        self.ventana.mainloop()
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todos = ""
            for posicion in self.listbox1.curselection():
                todos+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todos)
aplicacion1 = Aplicacion()












