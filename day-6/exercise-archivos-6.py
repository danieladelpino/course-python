registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Abrimos en modo append ("a") para agregar al final sin borrar lo anterior
archivo = open("registro.txt", "a")
archivo.writelines("\t".join(registro_ultima_sesion) + "\n")  # Agregamos salto de línea también
archivo.close()

# Leemos el contenido completo del archivo
archivo = open("registro.txt", "r")
print(archivo.read())
archivo.close()
