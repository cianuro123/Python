###
# 04 - Sets
# Los conjuntos son una forma de agrupar caracteres en una expresión regular.
# Se utilizan para especificar un conjunto de caracteres que pueden coincidir en una posición dada.
###

import re
from os import system
if system("clear") != 0:
    system("cls")

# [:] Coincide con cualquier carácter en el conjunto definido por los caracteres dentro de los corchetes.

# username = "user12_XX.3"
# pattern=r"^[\w._%+-]+$"

# matches = re.findall(pattern, username)
# if matches:
#     print(f"Coincidencias encontradas: {matches}")
# else:
#     print("No se encontraron coincidencias.")

# #Buscar las vocales en una cadena de texto
# text = "Hola, ¿como estas?"
# pattern = r"[aeiou]"
# matches = re.findall(pattern, text)
# print(matches)  # ['o', 'a', 'o', 'o', 'e', 'a']

# #Una Regex para encontrar las palabras man, fan y ban pero ignora el resto

# text="man, fan, ban, can, ran"
# pattern = r"[mfb]an"
# matches = re.findall(pattern, text)
# print(matches)  # ['man', 'fan', 'ban']

# #[^] Coincide con cualquier carácter que no esté en el conjunto definido por los caracteres dentro de los corchetes.

# text = "Hola, ¿como estas?"
# pattern = r"[^aeiou]"
# matches = re.findall(pattern, text)
# print(matches)  # ['H', 'l', ',', ' ', '¿', 'c', 'm', ' ', 's', 't', 's', '?']

# # Ejercicio final con todo lo aprendido
# # Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

#  Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

pattern = r"[\w.%_áéíúóñ+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}\.?[a-zA-Z]{2,}"
text = "lo.que+sea@shopping.online , michael@gov.co.uk , michael@gov.co.uk.%4"
matches = re.findall(pattern, text)
if matches:
    print(f"{matches}")
else:
    print("No se encontraron coincidencias.")
