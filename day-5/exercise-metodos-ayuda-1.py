# Texto original
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

# Caracteres que queremos remover del inicio
caracteres_a_remover = ",:_#%"

# Usamos lstrip pasando los caracteres como argumento
resultado = texto.lstrip(caracteres_a_remover)

# Mostramos el resultado
print(resultado)
