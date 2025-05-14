###
# Los Metacaracteres
# Son simbolos especiales con significados especificos en las expresiones regulares
###

import re

# 1. El punto (.)
# Coincidir con cualquer caracter excepto una nueva linea
text = "h0la que tal, H9la de nuevo, H¬la si, h0La"

pattern = "H.la"  # H0la, H@la, Hpla

found = re.findall(pattern, text, re.IGNORECASE)
print(found)

text = "cosa, caaasa, cisa, casa, causa"

# El punto refiere a un solo caracter, es un comodin de un solo espacio.
pattern = "c.sa"
print(re.findall(pattern, text))

# -------------------------------
text = "h0la que tal, H9la de nuevo, H¬la si, h0La"

pattern = r"H.la"  # H0la, H@la, Hpla

found = re.findall(pattern, text, re.IGNORECASE)
print(found)

# como usar la \ para ignorar el valor de un simbolo especial
text = "mi casa es blanca. y el coche es negro."
pattern = r"\."
matches = re.findall(pattern, text)
print(matches)

# \d: coincide con cualquier digito: (0,9)

text = "el numero de telefono es: 123456789"
found = re.findall(r'\d{9}', text)
print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "+324434343+423214+52134+34 3432343234+3445343453454-3452134432444"
pattern = r'\+34 \d{9}'
matchess = re.search(pattern, text)
if matchess:
    print(f"Encontré los siguientes números telefónicos:\n{matchess.group()}")
else:
    print("No encontré coincidencias")

# \w Coincide con cualquier caracter alfanumérico: (a-z, A-Z, 0-9,_)

text = "Elrubius_69"
pattern = r'\w'
matches = re.findall(pattern, text)
print(matches)

# \s Coincide con cualquier espacio en blanco: (espacio, tabulación, nueva línea)
pattern = r'\s'
text = "Este es un texto con espacios."
matches = re.findall(pattern, text)
print(matches)

# ^ Coincide con el inicio de una cadena
text = "$capo"
# Coincide con el primer caracter de la cadena modificando el funcionamiento del \w
pattern = r'^\w'
matches = re.findall(pattern, text)
if matches:
    print(f"El usuario es valido")
else:
    print("El usuario no es valido")

text = "+34 4343434343233+423214+52134+34 3432343234+34 45343453454-3452134432444"
pattern = r'^\+\d{1,3} '
matchess = re.search(pattern, text)
if matchess:
    print(f"Encontré los siguientes números telefónicos:\n{matchess.group()}")
else:
    print("No encontré coincidencias")

# $ Coincide con el final de una cadena
text = "Elrubius_69$"
# Coincide con el último caracter de la cadena modificando el funcionamiento del \w
pattern = r'^\w$'
matches = re.findall(pattern, text)
if matches:
    print(f"El usuario es valido")
else:
    print("El usuario no es valido")

# EJERCICIO:
# Tenemos una lista de archivos, y necesitamos saber los nombres de los archivos con extension .txt
# Ejemplo: ["archivo.txt", "archivo2.doc", "archivo3.txt"]

lista = ["archivo.txt", "archivo2.doc", "archivo3.txt"]

pattern = r'\.txt$'
matches = []
for i in lista:
    if re.search(pattern, i):
        matches.append(i)
print(matches)

# \b Coincide con el inicio o el final de una palabra
# Ejemplo: "Hola, soy un texto de prueba. Hola, soy un texto de prueba."

text = "Hola, soy un Holandes de prueba. Hola, soy un texto de prueba."
pattern = r'\bHola\b'
matches = re.findall(pattern, text)
print(matches)

# | Coincide con cualquiera de las opciones separadas por el símbolo |

fruits = "manzana, pera, naranja, uva, piña, sandía, uva, pera"
pattern = r"pera|uva|sandía|"  # imprime solo las frutas que coinciden con el patrón
# En este caso, el patrón coincide con cualquiera de las frutas especificadas
matches = re.findall(pattern, fruits)
print("Frutas encontradas:", matches)

# se pueden utilizar los | como un 'o' logico.
