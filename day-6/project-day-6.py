import os
from pathlib import Path

def mostrar_bienvenida():
    nombre_usuario = input("¡Hola!, ¿Cuál es tu nombre? ")
    print(f"\n¡Bienvenido {nombre_usuario} a nuestro Recetario!\n")

def acceso_recetario():
    ruta_recetas = Path("C:/Users/Personal/Recetas")
    print(f"La ruta de acceso a la carpeta de recetas es:\n{ruta_recetas}\n")
    return ruta_recetas

def contar_recetas(ruta):
    total = len(list(ruta.rglob("*.txt")))
    print(f"En total hay {total} receta(s) en la carpeta.")


while True:
    limpiar_consola()
    mostrar_bienvenida()
    mostrar_ruta()
    contar_recetas()
    mostrar_menu()
    
    eleccion = input("Elegí una opción: ")
    
    if eleccion == "1":
        leer_receta()
    elif eleccion == "2":
        crear_receta()
    elif eleccion == "3":
        crear_categoria()
    elif eleccion == "4":
        eliminar_receta()
    elif eleccion == "5":
        eliminar_categoria()
    elif eleccion == "6":
        print("¡Chau!")
        break
    else:
        print("Opción inválida.")
    
    input("Presioná cualquier tecla para volver al menú.")

os.system("cls")