import os
os.system("cls")
###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
numero = 10
while numero > 0:
    print(numero)
    numero -= 1
# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numero = 1
suma_numero = 0
while numero <= 20:
    if numero % 2 == 0:
        suma_numero += numero
    numero += 1
print(f"el resultado es: {suma_numero}")
# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
res=1
while True:
    try:
        factorial=int(input("Escribe un numero para saber el factorial: "))
        if factorial<=0:
            print("tu numero debe ser mayor a 0")
        res=factorial
        while factorial>1:
            res*=factorial-1
            factorial-=1
    except:
        print("Debes ingresar un número, no es tan dificil.")
        continue
    print(f"El factorial de tu numero es {res}")
    break
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
while True:
    contraseña=str(input("Escriba una contraseña con al menos 8 carácteres: \n"))
    if len(contraseña)<=8:
        print("Tu contraseña debe tener al menos 8 carácteres.\n")
        continue
    print("Contraseña válida.")
    break

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
tabla= []
contador = 1
numero=int(input("Escribe un número para ver su tabla de multiplicar: "))
while len(tabla) < 10:
    try:
        if numero <=0:
            print("El numero debe ser mayor a 0.")       
    except:
        print("Por favor, vuelva a ingresar un número")
        continue
    tabla+=[numero*contador]
    contador +=1
print(f"La tabla de multiplicar de su numero es:\n {tabla}")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
N = int(input("Escribe un numero entero: "))
contador = 1
primos=1
#Sin resolver.


#solucion de midudev
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1
