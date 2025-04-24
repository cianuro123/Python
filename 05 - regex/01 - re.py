"""
Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda.
Se utilizan  para la busqueda de cadenas de texto, validacion de datos, etc

# Por que aprender Regex?
- Busqueda avanzada: Encontrar patrones de busqueda en cadenas de texto muy grandes de forma rapida y precisa. (un editor
de Markdown solo usando Regex)

- Validacion de datos: Asegurar que los datos ingresados por el usuario son correctos. (email, telefono, direccion, contraseñas, etc)

-Manipulacion de texto: Poder modificar, reemplazar y extraer partes de las cadenas de texto facilmente.
"""
import os
os.system("cls")
import re
# 1 - Importar el modulo de expresiones regulares:
# Establecer en una variable el patron a buscar
pattern = "Hola"
# Establecer en otra variable el texto donde queremos buscar
text = "Hola Mundo"
# crear una variable para el ejecutar la funcion de busqueda de re.
result = re.search(pattern, text)  # re.search(patron, texto)
# Devuelve un tipo de dato "Match".<class 're.Match'>

if result:
    print("He encontrado el patron en el texto")
else:
    print("No he encontrado el patron en el texto")

#.group devuelve la cadena que coincide con el patron
print(result.group())
#.start devuelve la posicion de incio de la coincidencia
result.start()
#.end devuelve la posicion final de la coincidencia
result.end()

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
  print(f"He encontrado el patrón en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
  print("No he encontrado el patrón en el texto")
  
#-------------------------------------------
#Encontrar todas las coincidencias de un patron en un texto

text="Me gusta el arte, el arte ilumina el atardecer. El arte es artistica contractual, arte que ilumina, el arte es cagarse de frio."
pattern= "arte"
matches=re.findall(pattern, text)
print(len(matches))

#-------------------------------------------
#iter() devuelve un iterador que contiene todos los resultados de la busqueda
text="Me gusta el arte, el arte ilumina el atardecer. El arte es artistica contractual, arte que ilumina, el arte es cagarse de frio."
pattern= "arte"
matches=re.finditer(pattern,text)

for match in matches:
    print(match.group(), match.start(), match.end())
    
# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

#encontrar ocurrencias de "midu"
#indicar posicion inicial y final de cada una
# cuantas veces se encontro la ocurrencia

patron = "midu"
ocurrencias = re.finditer(patron, text)
for match in ocurrencias:
    print(f"Se ha encontrado el siguiente patron:\n{match.group()}\nSe ha encontrado en la posicion {match.start()} hasta {match.end()}\n")   
print(f"Se ha encontrado el patron '{patron}' {len(re.findall(patron,text))} veces")

#---------------------------
#Modificadores
#Los modificadores son opciones que le podemos agrega a un patron para cambiar su comportamiento
#re.IGNORECASE: Ignora las mayusculas y minusculas
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado. La iA es increible, parece Ia sin hacer cuando la ia hace"
pattern = "IA"
found_ia = re.findall(pattern, text,re.IGNORECASE)


if found_ia:
    print(f"He encontrado el patrón: {found_ia}")
else:
    print("No he encontrado el patrón en el texto")
    
# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

pater="python"
resulta=re.findall(pater,text, re.IGNORECASE)
print(resulta)

##Remplazar el texto
#.sub() reemplaza todas las coincidencias de un texto

text="hola mundo, hola a todos. Hola gente y hola gentuza"
patron="hola"
replacement="adios"

now_text=re.sub(patron,replacement,text,count=3,flags=re.IGNORECASE) 
#count= asigna cuantas coincidencias va a reemplazar. Y flags= sirve para poner las opciones, sino da error.
print(now_text)
