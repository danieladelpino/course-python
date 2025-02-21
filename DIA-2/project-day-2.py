"""
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones.

 Este programa debería comenzar preguntando cosas al usuario, por lo tanto, vas a
necesitar input para poder recibir los ingresos del usuario y deberías usar variables para
almacenar esos ingresos. Recuerda que los ingresos de usuarios se almacenan como
strings. Por lo tanto, deberías convertir uno de esos ingresos en un float para poder hacer
operaciones con él.

 ¿Y qué operaciones necesitas hacer? Bueno, calcular el 13% del número que haya
ingresado el usuario. Es decir, que debes multiplicar ese número por 13 y luego dividirlo
por 100. Recuerda almacenar ese resultado en una variable.

 Sería bueno que para imprimir en pantalla el resultado te asegures de que esa
información no tenga más de dos decimales, para que sea fácil de leer, y luego organiza
todo eso en un string al que debes dar formato. Recuerda que conocimos dos maneras
de hacerlo y cualquiera de ellas es válida. 
"""


nombre = input("¿Cuál es tu nombre? ")
ventas = int(input("¿Cuánto has vendido este mes? "))

comision = round(ventas * 13 / 100, 2)

print(f"{nombre}, tu comisión por las ventas de este mes es: ${comision}")
