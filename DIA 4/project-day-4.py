from random import *

nombre_usuario = input("¿Cuál es tu nombre? ")
print(f"{nombre_usuario}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

numero_secreto = randint(1, 100)
intentos = 8

while intentos > 0:
    numero_usuario = int(input("Ingresa un número: "))
    
    if numero_usuario < 1 or numero_usuario > 100:
        print("Ha elegido un número que no está permitido.")
        continue
    
    intentos -= 1 
    
    if numero_usuario == numero_secreto:
        print(f"¡Has ganado! El número secreto era {numero_secreto} y lo has logrado en {intentos} intento(s).")
        break
    
    elif numero_usuario < numero_secreto:
        print(f"Tu respuesta es incorrecta y has elegido un número menor al número secreto. Te quedan {intentos} intento(s).")
    elif numero_usuario > numero_secreto:
        print(f"Tu respuesta es incorrecta y has elegido un número mayor al número secreto. Te quedan {intentos} intento(s).")
else:
    print(f"¡Te quedaste sin intentos! El número secreto era: {numero_secreto}.")
