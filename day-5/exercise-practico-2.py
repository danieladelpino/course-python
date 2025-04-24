"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
"""

def letras_unicas(palabra):
    # Paso 1: Eliminar letras duplicadas usando un conjunto (set)
    letras = set(palabra)
    
    # Paso 2: Convertir el conjunto a una lista y ordenarla alfabéticamente
    letras_ordenadas = sorted(letras)
    
    return letras_ordenadas

print(letras_unicas("entretenido"))
