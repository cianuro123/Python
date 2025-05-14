import os
os.system("cls")

#  -- 02 - Bucles For
#  --- Permite ejecutar un bloque de codigo mientras ITERA un "ITERABLE" o una lista.
### 
print("\nBucles For:")

#Iterar una lista
print("/////////////////////\nIterar una lista:")
frutas = ["manzanas", "peras", "mandarinas", "lechugas"] #obviamente la lechuga es una fruta😒

for fruta in frutas: 
    print(fruta)

#Iterar sobre cualquier cosa que sea Iterable
print("\nIterar una cadena de texto:")
cadena = "thiagopro"

for caracter in cadena:
    print(caracter)

#enumerate()
print("\nBucles for usando enumerate():")
frutas = ["manzanas", "peras", "mandarinas", "lechugas"]
 ##   1er | 2da   (posicion)##
for index, fruta in enumerate(frutas): 
    print(f"El indice es {index} y la fruta es {fruta} ")
#de esta forma, estamos mostrando el index de cada elemento de la lista y mostrando el elemento de cada index.
#el enumerate() pone en la primer posicion (index) el valor de index y en la segunda posicion (fruta) el elemento de
#ese indice

#bucles anidados
print("\nBucles Anidados:")
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

#Break
print("\nUso del break:")

dioses = ["tralalero tralala", "thung thung thung thung sahur", "lirili larila","bombardiro crocodiro" ]

for idx, dios in enumerate(dioses):
    if dios=="lirili larila": 
        print(f"Joven Aventurero.— \"D-D-DIOS?!\"\nDios le contesta:\nDios.— \"Si.. Yo soy... {dios}{idx}")
    break   
#Continue
print("\nUso del Continue:")

dioses = ["tralalero tralala", "thung thung thung thung sahur", "lirili larila","bombardiro crocodiro" ]

for idx, dios in enumerate(dioses):
    if dios=="lirili larila":continue#podemos omitir cierto elemento de una lista usando continue. 
                                     #Se puede poner el continue en la misma linea del if
    print(dios.upper())
    
#Comprensión de listas (List Comprehension)
print("\nComprension de listas:")
animales =["perro", "gato","pez","pinocho"]

animales_mayus=[animal.upper() for animal in animales]
print(animales_mayus,"\n")

#Muestra los numeros pares de una lista

pares=[num for num in [1,2,3,4,5,6,7,8,9,10] if num%2==0] 
print(pares)
#comprension de una lista mas un condicional