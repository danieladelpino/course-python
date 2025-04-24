lista_numeros = [1, 2, 15, 7, 2, 8]

def reducir_lista(lista):
    lista = list(set(lista))  # Elimina duplicados
    lista.sort()               # Ordena la lista
    lista.pop(-1)              # Elimina el valor más alto
    return lista              # Devuelve la lista modificada

def promedio(lista):
    valor_medio = sum(lista) / len(lista)  # Calcula el promedio
    return valor_medio                    # Devuelve el promedio
