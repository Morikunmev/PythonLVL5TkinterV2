archi1 = open("datos.txt","a")
archi1.write("nueva linea \n")
archi1.write("nueva linea \n")
archi1.close()
archi1 = open("datos.txt","r")
contenido = archi1.read()
archi1.close()
print(contenido)