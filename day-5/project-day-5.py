from random import choice

# Lista de palabras
lista_palabras = ["mesa", "silla", "televisor", "cama"]

def seleccion_palabra(lista):
    return choice(lista)

def mostrar_guiones(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    print(resultado.strip())

def pedir_letra():
    while True:
        letra = input("Elegí una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Ingresá solo una letra, por favor.")

def jugar():
    palabra = seleccion_palabra(lista_palabras)
    letras_adivinadas = []
    vidas = 6

    print("¡Bienvenid@ al Ahorcado! 🎉 Tenés 6 vidas.")
    
    while True:
        mostrar_guiones(palabra, letras_adivinadas)

        letra = pedir_letra()

        if letra in letras_adivinadas:
            print("Ya dijiste esa letra 😅")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien! La letra está en la palabra 🤩")
        else:
            vidas -= 1
            print(f"Ups... esa letra no está 😖. Te quedan {vidas} vidas.")

        # 🟢 Verificar si ganó
        if all(l in letras_adivinadas for l in palabra):
            print(f"¡Ganaste! La palabra era: {palabra} 🥳")
            break

        # 🔴 Verificar si perdió
        if vidas == 0:
            print(f"Perdiste 💀 La palabra era: {palabra}")
            break

# Iniciar juego
jugar()
