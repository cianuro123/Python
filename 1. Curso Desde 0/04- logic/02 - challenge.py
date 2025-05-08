import os
os.system("cls")

"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""


def suma_pares(numeros):
    result=0
    for i in numeros:
        if i % 2 == 0:
            result+=i
    return result
list=[1,2,5,23,5,2,455,54,22,45,34,53,100]
print(suma_pares(list))