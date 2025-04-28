def sobrescribir(archivo):
    sobreescritura = open(archivo, "w")
    sobreescritura.write("contenido eliminado")
    sobreescritura.close()
