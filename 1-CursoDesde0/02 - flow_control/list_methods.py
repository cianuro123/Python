import os
os.system("cls")

# Metodos más importantes para trabajar con listas
print("Metodos para trabajar con listas:")
print("\nAgregar o insertar elementos a una lista:")
print("\"append\"")
lista = [1, 2, 3, 4, 5]
lista.append(6)  # añade un solo elemento al final (limite 1)
print(lista)

print("\n\"insert\"")
lista.insert(2, "$")  # Inserta un valor en la posicion indicada
# (posicion, valor)
print(lista)

print("\n\"extend\"")
lista.extend([5, "hola", 5.434])  # Extiende la lista a partir del final
# sin limite de elementos (sin limite)
print(lista)

# Remover o eliminar elementos de una
print("----------------------------\nEliminar elementos de una lista:")
print("\"remove\"")
lista = [1, 2, 3, 4, 5, 6, '%', 7, '%']
print("- sin .remove\n", lista)
lista.remove('%')  # elimina la primera aparicion del elemento dado.
# Elimina elementos no indices.
print("- con .remove\n", lista)

print("\n\"pop\"")
ultimo = lista.pop()  # elimina el ultimo indice de la lista y lo devuelve
print(lista)
print(ultimo)

# se pueden usar numeros negativos y borra de derecha a izquierda la posicion dada
pop3 = lista.pop(-3)
print(lista)
print(pop3)

print("\n\"del\"")
print(lista)
del lista[2]  # elimina la posicion determinada
print(lista)
del lista[0:2]  # con del se pueden eliminar rangos de elementos x indice
print(lista)

print("\n\"clear\"")
lista.clear()  # elimina todos los elementos de la lista
print(lista)

print("----------------------------\nMás métodos útiles:")
print("\"sort\" modificando la lista original:")
lista = [45, 23, 71, 212, 2, 4, 0.1]
print(lista)
lista.sort()
print(lista)# ordena los elementos de la lista modificandola, no la devuelve
print("\n\"sorted\" creando una nueva lista:")
# Crea una copia ordenada de la lista y la devuelve
lista = [45, 23, 71, 212, 2, 4, 0.1]
print(f"Original: {lista}")
sorted_numbers = sorted(lista)
print("Ordenada:", sorted_numbers)

frutas = ["peras", "Manzanas", "Uvas", "frijoles",
          "chimangos", "Jamoncito", "manzanas", "uvas"]
# Ordena las mayusculas primero por su valor numérico. (a!=A), (b!=B), etc
sorted_frutas = sorted(frutas)
print("Frutas old:\n", frutas)
print("\nFrutas new: \n", sorted_frutas)
frutas.sort(key=str.lower)  # Transforma la cadena a lower keys
# logrando que queden ordenadas correctamente
print("\nFrutas c/sort key=lower:\n", frutas)

# Mas cositas utiles
animals = ["🐶", "😹", "🐼", "🦁"]
print(len(animals))  # ---> 4 * el numero de elementos de la lista

print(animals.count("🐼"))# ->1 * el numero de apariciones de ése elemento en la lista

print("🦜" in animals)# ----> False porque no aparece ese elemento en la lista.
