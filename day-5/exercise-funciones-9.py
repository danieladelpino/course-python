def cantidad_pares(lista):
    cantidad_de_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            cantidad_de_pares += 1
    return cantidad_de_pares
        
lista_numeros = [20,30,40,50,60]