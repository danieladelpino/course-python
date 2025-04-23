def suma_menores(lista):
    total = 0  # Declaramos la variable total fuera del ciclo
    for numero in lista:
        if numero > 0 and numero < 1000:  # Condición de que el número esté entre 0 y 1000
            total += numero  # Sumamos el número a total
    return total  # Devolvemos el total al final

lista_numeros = [1, 2, 3, 1500, -10]  # Ejemplo de lista con algunos números fuera de rango
