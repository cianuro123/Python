import os
os.system("cls")

###
# 04 - Funciones
# Bloques de codigo reutilizables y parametizables para hacer tareas
# espicificas
###

"""
Definir una funcion

def nombre_de_la_funcion(parametro1,parametro2,parametro3,......)
    # docstring
    #cuerpo de la funcion
    return valor_de_retorno # opcional

"""

#Ejemplo de una funcion para imprimir algo en consola
print("\nPrincipio de funciones\n")
def saludar():
    print("hola soy una funcion")
    
saludar()
saludar()
saludar()

print("\nFunciones con 'Parametros'")
def saludar_a(nombre): #"nombre" es el parámetro de la funcion
    print(f"hola {nombre}")
    
saludar_a("jose") #lo que pongamos dentro del parentesis seran los argumentos
saludar_a("juan")
saludar_a("toallin")

#El parámetro es lo que acepta la funcion
#El argumento es lo que muestra la funcion

#Funciones con más parametros
print("\nFunciones con más de 1 parámetro")
def sumar(a,b):
    suma=a+b
    return suma

result=sumar(2,5)
print(result)
### Otra forma 
#print(sumar(2,5)) Depende de si la funcion tiene "return" o no

#Documentar las funciones con Docstring
def restar(a,b):
    """Resta dos numeros y devuelve el resultado""" #Descripcion de la funcion!!!
    return(a-b)

# help(restar)

# parametros por defecto
def multiplicar(a,b =2):
    return a*b

print(multiplicar(2)) #sin especificar multiplica por 2 por defecto y da 4
print(multiplicar(2,3)) #igualmente si se especifica se puede cambiar

def describir_persona(nombre,edad,sexo):
    print(f"Me llamo {nombre} mi edad es {edad} años y me identifico como {sexo}")

#Los parametros son posicionales
describir_persona(20, "Thiago", "hombre")
describir_persona("hombre", 43, "Juan")

#Argumentos por clave
#Parametros nombrados
describir_persona(sexo="C++", nombre="Qiricocho", edad="32^1000000")
describir_persona(edad=18, nombre="Thiago", sexo="hombre")

#Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma=0
    for numero in args:
        suma+= numero
    return suma

print(sumar_numeros(1,2,3,6,4,4,623,5))
print(sumar_numeros(3,2,55,62,1))
print("\n")

#Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor, in kwargs.items():
        print(f"{clave}: {valor}")
        
mostrar_informacion_de(le_gustan_los_tacos=True, edad=20, ronronea=True)
print("\n")
mostrar_informacion_de(nombre="Raul", pais="Oceania", le_gustan_los_chimangos=True)
