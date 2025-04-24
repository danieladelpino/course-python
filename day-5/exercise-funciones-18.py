def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for atributo, valor in kwargs.items():
        print(f"{atributo}: {valor}")
