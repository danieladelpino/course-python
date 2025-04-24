"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def numero_cero(*args):
    for i in range(len(args) - 1):  # Compara el número actual con el siguiente
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False

# Pruebas
print(numero_cero(5, 6, 1, 0, 0, 9, 3, 5))  # Debería devolver True
print(numero_cero(6, 0, 5, 1, 0, 3, 0, 1))  # Debería devolver False
