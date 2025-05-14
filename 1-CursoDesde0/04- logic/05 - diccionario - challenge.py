"""

Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"

"""
from os import system
if system != "clear": system("cls")  
def battle(lista_a, lista_b):
    valor_sig_idx = 0
    for index, _ in enumerate(lista_a):
        if len(lista_b) != len(lista_a): return print("Error: Las listas deben tener igual longitud") #Return rapido si no cumple la condicion   
        if valor_sig_idx < len(lista_a)-1: valor_sig_idx += 1 #Evita que el valor del index se pase de rango
        diferencia = abs(lista_a[index] - lista_b[index])
        if lista_a[index] > lista_b[index]:
            lista_a[valor_sig_idx] = diferencia + lista_a[valor_sig_idx]
        else:
            lista_b[valor_sig_idx] = diferencia + lista_b[valor_sig_idx]
    if lista_b[valor_sig_idx] == lista_a[valor_sig_idx]:
        return print("X")
    elif lista_a[valor_sig_idx] > lista_b[valor_sig_idx]:
        return print(f"{diferencia}a")
    else:
        return print(f"{diferencia}b")
lista_a = [2, 5, 2]
lista_b = [3, 3, 3]
battle(lista_a, lista_b)
