archi1 = open("datos.txt","r")
lineas = archi1.readlines()
print("La cantidad de lineas que tiene el archivo de texto: ",len(lineas))
print("Contenido del archivo de texto")
for linea in lineas:
    print(linea,end="")