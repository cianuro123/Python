import os
os.system("cls")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
pares=[num for num in [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]if num%2==0]
print(pares)
pares=[num for num in range(0,21,2)]
print(pares)
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
sumador = 0
contador = len(numeros) #DE MAS
for num in numeros:
    sumador+=num
    contador-=1                 #DE MAS
    if contador == 0:           #DE MAS
        sumador//=len(numeros)   
        print(f"la media es: {sumador}")
        
###CORRECION:       
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
  suma += numero
media = suma / len(numeros)
print(f"La media es: {media}")


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
num_mayor = numeros[0]
for num in numeros:
    if num > num_mayor:
        num_mayor = num
print(f"El número mayor es: {num_mayor}")
# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas=[palabra for palabra in palabras if len(palabra)>5]
print(palabras_largas)
# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche",]
letra=str(input("Escribe una letra: ")).lower()#correccion
#letra=letra.lower() No es necesario
igualdades=0
attemps = len(palabras)
for palabra in palabras:
    for index,letter in enumerate(palabra):
        if letra == letter and index == 0:
            igualdades +=1
        else:
            break
    attemps-=1
    if attemps == 0:
        print(f"Las igualdades encontradas son: {igualdades}")
    continue
