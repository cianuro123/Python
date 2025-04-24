import os
os.system("cls")

###
# Consigna: Elegir 6 ejercicios anteriores y rehacerlos usando funciones.
# Objetivo: Lograr utilizar todos los casos vistos hasta el momento.

print("Ejercicio 1:")
#Ej 1:
# Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10).
def multiplicar(a):
    for i in range(0,11):
        mult=i*a
        print(mult)
    return mult
try:
    n=int(input("Escribe un numero: "))
    multiplicar(n)
    
except:
    print("No es un numero")
        
print("Ejercicio 2:")  
# Ejercicio 2: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Si la contraseña es válida, imprime "Contraseña válida".

def contraseña(password):
    while True:
        if len(password) < 8:
            password=input("Ingrese una contraseña de al menos 8 carácteres: ")
            continue
        elif len(password) >= 8:
            print("Contraseña Valida")
            break
a=input("Ingrese una contraseña de al menos 8 carácteres: ")
contraseña(a)

print("\nEjercicio 5:")
# Ejercicio 5: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
def maximo(*args):
    maximos=args[0]
    for i in args:
        if i > maximos:maximos=i
        else: continue
    print(f"El numero maximo es: {maximos}")
maximo(343,432,51,31,5)
print("Ejercicio 3:")


print("Ejercicio 4:")

print("Ejercicio 5:")

print("Ejercicio 6:")