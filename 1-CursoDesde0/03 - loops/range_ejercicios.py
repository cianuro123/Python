import os
os.system("cls")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for i in range(1, 11):
    print(i)
# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for i in range(1, 21, 2):
    print(i)
# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for i in range(5, 51, 5):
    print(i)
# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for i in range(10, 0, -1):
    print(i)
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
for i in range(1, 101):
    res = (i*(i+1))//2  # Formula de Gauss😜
print("la suma de los numeros del 1 al 100 es:",res)
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Escribe un numero: "))
print(f"La tabla del {numero} es:")
for num in range(1, 11):
    print(num*numero)