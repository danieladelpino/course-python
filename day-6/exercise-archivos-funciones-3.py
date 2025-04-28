def registro_error(archivo):
    registro = open(archivo, "a")
    registro.write("se ha registrado un error de ejecución")
    registro.close()
