from os import system
if system("clear") != 0:
    system("cls")

# CONDICIONALES
#Teoria:
# Tabla de la verdad (para Referencia)

print("Tabla de la verdad:\n")
print("and:")  # Busca que se cumplan las 2 condiciones (2 True)
print("A      B      A and B")
print("True   False ",   True and False)
print("False  True  ",    False and True)
print("True   True  ",    True and True)
print("False  False ",   False and False)

print("\nor:")  # Busca que se cumpla al menos una de las condiciones (1 True)
print("A      B      A or B")
print("True   False ",   True or False)
print("False  True  ",    False or True)
print("False  False ",   False or False)
print("True   True  ",    True or True)

# Invierte el valor inicial (si era True => False y si era False => True)
print("\nnot:")
print("A      not A")
print("False ", not False)
print("True  ", not True)

# Los numeros tambien pueden ser booleanos y por lo tanto condicionales.
# Cualquier número != 0 va a ser True

numero=4 #True
if numero:
    print("no es cero")
numero=-10 #Los negativos tambien son True
if numero:
    print("negativos tambien son True")
numero =0 #0 = False
if numero:
    print("por aca no pasa")
numero="" #Vacio = False
if numero:
    print("No va a printar esto")

#Practica
# Ejercicio 1: Pedir 2 numeros y mostrar el mayor o igual
print("Ejercicio 1:")
numero1 = input("Escriba un numero a continuacion: ")
numero2 = input("Escriba otro numero a continuacion: ")
if numero1 == numero2:
    print("Son iguales")
elif numero1 >= numero2:
    print("Tu primer número es mayor")
else:
    print("Tu segundo numero es mayor")

# Ejercicio 2: Calculadora sencilla solucionando div. por 0.
print("Ejercicio 2:")
num1 = input("diga su primer entero: ")
num1 = int(num1)
op = input("Establece la operacion; Sum(+), Res(-), Mult(*), Div(/): ")
num2 = input("diga su segundo entero: ")
num2 = int(num2)
if op == "+" or op == "sum":
    print(num1+num2)
elif op == "-" or op == "res":
    print(num1-num2)
elif op == "*" or op == "mult":
    print(num1*num2)
else:
    if num2 == 0:
        print("Indeterminado")
    else:
        print(num1/num2)

# Ejercicio 3: Pedir un año y mostrar si es biciesto o no.
print("Ejercicio 3:")
año = input("Escriba un año: ")
año = int(año)

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("Es biciesto")
else:
    print("No lo es")

# Ejercicio 4: Pedir una edad y decir si es bebe [0,2],
# niño [3, 12], adolescente [13, 17], adulto [18, 64],
# adulto mayor [65, ∞]
print("Ejercicio 4:")
edad = input("Ingrese una edad: ")
edad = int(edad)
if edad <= 2 and edad >= 0:
    print("Es bebé")
elif edad >= 3 and edad <= 12:
    print("Es niño/a")
elif edad >= 13 and edad <= 17:
    print("Es adolescente")
elif edad >= 18 and edad <= 64:
    print("Es adulto")
elif edad > 65:
    print("Es adulto mayor")


