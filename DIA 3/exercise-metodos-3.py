"""
Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.
"""

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase_modificada = frase.replace("difícil", "fácil").replace("mala", "buena")
print(frase_modificada)