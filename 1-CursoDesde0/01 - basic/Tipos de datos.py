from os import system
import math
if system("clear") != 0:
    system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# Completa aquí

print("Hola soy Thiago\nSoy de Puerto Madryn")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

# Completa aquí

print('a es:', type(a), "\nb es:", type(b), "\nc es:",
      type(c), "\nd es:", type(d), "\ne es:", type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# Completa aquí
a1=12345
b1=3.99

print(int(a1))
print(float(a1))
print(int(b1))
# Lo que ocurre es que, al convertirlo, se eliminan los decimales quedando 3, lo cual es un error ya que está mas cerca de 4.

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

# Completa aquí
name: str = "Thiago"
edad: int = "18"
altura: float = "1.80"
print(f"Hola, me llamo {name}, tengo {edad} años y mido {altura} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

#Completa aqui
PI = 3.1416  #Se usan "." y no "," para expresar decimales.
round(PI)
print(int(PI) // 2)

# Importo la libreria "math" para acceder al numero pi y asi hacer la division sin utilizar variables
print(round(math.pi))
print(int(math.pi / 2))
