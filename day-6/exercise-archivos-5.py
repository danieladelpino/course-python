archivo = open("mi_archivo.txt", "a")
archivo.write("Nuevo inicio de sesión")
archivo.close

archivo = open("mi_archivo.txt", "r")
print(archivo.read())