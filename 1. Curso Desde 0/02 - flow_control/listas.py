import os
os.system("cls")
# listas
lista1 = [1, 2, 3, 4, 5]  # lista de enteros
lista2 = ["hola", "si", "que tal", "habla"]  # Lista de strings
lista3 = [1, "estilo", 3.32, False]  # lista mixta
lista_de_lista = [[1, 2, 3], ["coma", "mono", "hello"], [3.32, 4.5, 22.4]]
matriz = [[0, 2], [4, 2], [8, 1]]

print("Listas:")
print(lista1)
print(lista2)
print(lista3)
print(lista_de_lista)

# acceso a elementos por índice
print("\nAcceso por indice:")
print(lista1[2])
print(lista2[-2])  # El menos hace que vaya de atras para adelante (inverso)
print(lista_de_lista[2][2])
# El primer numero selecciona la lista, y el segundo la posición

# Slicing (rebanado) de listas
print("\nSlicing:")
# muestra la posición 1 de lista1 hasta la posición 2 (el 3 lo excluye)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1[1:3])
# muestra las dos ultimas posiciones
print(lista2[-2:])
# muestra las dos primeras
print(lista1[:2])
# El tercer elemento representa el "paso", que es la
# cant. de índices que deja de por medio entre cada elemento de la lista.
# Ej:
print(lista1[2::3])
# selecciona el punto de inicio en el índice 2, el siguiente valor al
# estar vacío representa todos los valores o, en este caso, "Hasta el final". Y el 3
# representa los pasos que dá entre índice e índice.
# El resultado entonces sería [3,6,9].

print(lista1[::-1])
#Hace que los pasos vayan al revés, mostrando la lista invertida
lista1[1]=20
#modifico el valor del indice 1 haciendolo igual a 20
print(lista1)
lista1[0]=lista1[3]+lista1[4] 
#modifico el valor del indice 0 asignandole el valor de la suma del indice 3 y el indice 4.
print(lista1)

lista1=[1,2,3,4,5,6,7,8,9]
#Forma de modificar una lista menos eficiente:
lista1=lista1+[10,11,12]#aqui se almacena en la memoria la operacion y luego se modifica la lista
print(lista1)
#Forma mas eficiente y corta
lista1+=[13,14,15,16]#aqui se modifica directamente la lista, sin almacenar la operación
print(lista1) #Al sumarle una lista, lo que hace python es concatenarla a la lista preexistente, haciendola única.

#Recuperar la LONGITUD de una LISTA
print("Recuperar la Longitud de una Lista")
lista1=[1,2,3,4,5,6,7,8,9,10,11]
print(len(lista1))
mitad=len(lista1)/2
print(mitad)



