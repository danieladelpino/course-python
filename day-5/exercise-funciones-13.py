def suma_cuadrados(*args):
    total = sum(arg**2 for arg in args)  # Sumar los cuadrados de los argumentos
    return total
    
print(suma_cuadrados(1, 2, 3))  # Debería devolver 14 (1^2 + 2^2 + 3^2)
