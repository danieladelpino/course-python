import os
from pathlib import Path
import shutil

def mostrar_bienvenida():
    nombre_usuario = input("¡Hola!, ¿Cuál es tu nombre? ")
    print(f"\n¡Bienvenido {nombre_usuario} a nuestro Recetario!\n")

def mostrar_ruta():
    ruta_recetas = Path("C:/Users/Personal/Recetas")
    print(f"La ruta de acceso a la carpeta de recetas es:\n{ruta_recetas}\n")
    return ruta_recetas

def contar_recetas(ruta):
    total = len(list(ruta.rglob("*.txt")))  # Busca todos los archivos con extensión .txt dentro de la carpeta y todas sus subcarpetas gracias a .rglob("*.txt")
    print(f"En total hay {total} receta(s) en la carpeta.")

def limpiar_consola():
    os.system("cls")

def mostrar_menu():
    print("¿Qué te gustaría hacer?")
    print("1. Leer una receta")
    print("2. Crear una nueva receta")
    print("3. Crear una nueva categoría")
    print("4. Eliminar una receta")
    print("5. Eliminar una categoría")
    print("6. Salir del recetario")

def leer_receta(ruta):
    # Mostrar las carpetas (categorías)
    print("Categorías disponibles:")
    for carpeta in ruta.iterdir():  # ruta.iterdir() recorre todos los elementos dentro de esa carpeta
        if carpeta.is_dir():  # carpeta.is_dir() filtra para mostrar solo las carpetas (no archivos).
            print(f"- {carpeta.name}")

    categoria = input("\nEscribí el nombre de la categoría que querés abrir: ")
    ruta_categoria = ruta / categoria

    if not ruta_categoria.exists():
        print("Esa categoría no existe.")
        return

    # Mostrar recetas
    print("\nRecetas disponibles:")
    for receta in ruta_categoria.glob("*.txt"):
        print(f"- {receta.stem}")  # stem te da el nombre sin la extensión .txt,

    nombre_receta = input("\nEscribí el nombre de la receta que querés leer (sin .txt): ")
    ruta_receta = ruta_categoria / f"{nombre_receta}.txt"

    if not ruta_receta.exists():
        print("Esa receta no existe.")
        return

    # Mostrar contenido
    print("\nContenido de la receta:\n") 
    with open(ruta_receta, "r") as archivo:
        contenido = archivo.read()
        print(contenido)

def crear_receta(ruta):
    print("Categorías disponibles:")
    for carpeta in ruta.iterdir():
        if carpeta.is_dir():
            print(f"- {carpeta.name}")

    categoria = input("\nElegí una categoría donde guardar la receta: ")
    ruta_categoria = ruta / categoria

    if not ruta_categoria.exists():
        print("Esa categoría no existe.")
        return

    nombre_receta = input("Escribí el nombre de la receta: ")
    contenido = input("Escribí el contenido de la receta:\n")

    ruta_archivo = ruta_categoria / (nombre_receta + ".txt")

    if ruta_archivo.exists():
        print("Ya existe una receta con ese nombre.")
        return

    with open(ruta_archivo, "w") as archivo:
        archivo.write(contenido)

    print("La receta se creó con éxito. 🥳")

def crear_categoria(ruta):
    nueva_categoria = input("Escribí el nombre de la nueva categoría: ")
    ruta_nueva = ruta / nueva_categoria

    if ruta_nueva.exists():
        print("Esa categoría ya existe.")
    else:
        ruta_nueva.mkdir()
        print(f"Categoría '{nueva_categoria}' creada con éxito. 🎉")

def eliminar_receta(ruta):
    categoria = input("Escribí el nombre de la categoría: ")
    ruta_categoria = ruta / categoria

    if not ruta_categoria.exists():
        print("Esa categoría no existe.")
        return

    receta = input("Escribí el nombre de la receta que querés eliminar (con .txt): ")
    ruta_receta = ruta_categoria / receta

    if ruta_receta.exists():
        os.remove(ruta_receta)
        print(f"Receta '{receta}' eliminada.")
    else:
        print("Esa receta no existe.")

def eliminar_categoria(ruta):
    categoria = input("Escribí el nombre de la categoría que querés eliminar: ")
    ruta_categoria = ruta / categoria

    if not ruta_categoria.exists():
        print("Esa categoría no existe.")
        return

    # Eliminar la categoría y todo su contenido (archivos y subcarpetas)
    shutil.rmtree(ruta_categoria)
    print(f"Categoría '{categoria}' y su contenido han sido eliminados.")

while True:
    limpiar_consola()
    mostrar_bienvenida()
    ruta_recetas = mostrar_ruta()  # Guardamos la ruta en la variable ruta_recetas
    contar_recetas(ruta_recetas)
    mostrar_menu()
    
    eleccion = input("Elegí una opción: ")
    
    if eleccion == "1":
        leer_receta(ruta_recetas)
    elif eleccion == "2":
        crear_receta(ruta_recetas)
    elif eleccion == "3":
        crear_categoria(ruta_recetas)
    elif eleccion == "4":
        eliminar_receta(ruta_recetas)
    elif eleccion == "5":
        eliminar_categoria(ruta_recetas)
    elif eleccion == "6":
        print("Gracias por visitar nuestro Recetario!")
        break
    else:
        print("Opción inválida.")
    
    input("Presioná cualquier tecla para volver al menú.")
