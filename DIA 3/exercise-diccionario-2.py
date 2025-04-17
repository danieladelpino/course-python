mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9, "points2": [10, 300, 15]}
}

def mostrar_segundo_valor_points2(diccionario):
    segundo_valor = diccionario["puntos"]["points2"][1]
    return segundo_valor

print(mostrar_segundo_valor_points2(mi_dict))
