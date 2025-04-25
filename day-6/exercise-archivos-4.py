# Escribimos en el archivo
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()

# Ahora lo abrimos para leerlo
archivo = open("mi_archivo.txt", "r")
print(archivo.read())  # Esto sí muestra el contenido
archivo.close()
