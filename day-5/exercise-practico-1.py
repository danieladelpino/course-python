"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""

def devolver_distintos(*args):
    mayor = 0
    menor = 0
    suma = sum(args)
    if suma > 15:
        mayor = max(args)
        return mayor
    elif suma < 10:
        menor = min(args)
        return menor
    else:
        return sorted(args)[len(args) // 2]
    

# Ejemplos:
print(devolver_distintos(3, 5, 8))  # Debería devolver 8 (mayor)
print(devolver_distintos(1, 2, 3))  # Debería devolver 1 (menor)
print(devolver_distintos(4, 6, 5))  # Debería devolver 5 (intermedio)