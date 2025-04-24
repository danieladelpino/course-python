import random

# Función que simula el lanzamiento de una moneda
def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

# Función que prueba suerte según el resultado del lanzamiento
def probar_suerte(lanzamiento, lista):
    if lanzamiento == "Cara":  # Si el resultado es "Cara"
        print("La lista se autodestruirá")
        return []  # Devuelve la lista vacía
    
    else:  # Si el resultado es "Cruz"
        print("La lista fue salvada")
        return lista  # Devuelve la lista intacta

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamar a la función lanzar_moneda para obtener el resultado
lanzamiento = lanzar_moneda()

# Llamar a probar_suerte con el resultado del lanzamiento y la lista
lista_final = probar_suerte(lanzamiento, lista_numeros)

# Mostrar la lista final
print(f"Resultado del lanzamiento: {lanzamiento}")
print(f"Lista final: {lista_final}")
