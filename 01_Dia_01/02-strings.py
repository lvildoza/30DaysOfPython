# Métodos en variables

texto = "Hola Leo"
# variable.upper = transformar a MAYUSCULAS
print(texto.upper())

# variable.lower = transformar a minuesculas
print(texto.lower())

# variable.find = busca en que posición del indice esta el dato indicado
print(texto.find("L"))

# variable.replace = reemplaza una cadena de texto por otra
print(texto.replace("Leo", "Ing."))

# el método replace no reemplaza el valor original de la variable
otra_variable = texto.replace("Hola Leo", "Tandil")
# Imprimo la variable original y concateno el mensaje para que sea mas "lindo"
print(texto + "! estas en", otra_variable + "?")

# el método "in" busca dentro del string el dato que indiquemos, nos devolvera True o False
print("Leo" in texto)

# concatenando string
print(texto + ", la letra L se encuentra en el indice:", texto.find("L"))
