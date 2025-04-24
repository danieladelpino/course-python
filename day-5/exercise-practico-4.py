"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

def contar_primos(num):
    primos = []

    for n in range(2, num + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primos.append(n)
    
    print("Números primos encontrados:", primos)
    return len(primos)

# Prueba
print("Cantidad de primos:", contar_primos(20))
