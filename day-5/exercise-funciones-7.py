def todos_positivos(lista):
    for elemento in lista:
        if elemento <= 0:  # Si encontramos un número negativo o 0
            return False
    return True  # Si no encontramos números negativos, devuelve True

lista_numeros = [1, 2, 3, 4, 5]  # Ejemplo con todos positivos
