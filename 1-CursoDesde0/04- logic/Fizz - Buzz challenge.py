""""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
from os import system
if system("clear") != 0:
    system("cls")
numeros:list = (range(1, 101))

def fizzbuzz(lissta):
    lista=list(lissta)
    for idx,i in enumerate(lista):
        if i%5 == 0 and i%3 == 0:
            lista[idx]="fizzbuzz"
            continue
        if i%3==0:
            lista[idx]="fizz"
        if i%5==0:
            lista[idx]="buzz"
    return (lista)
print(fizzbuzz(numeros))
