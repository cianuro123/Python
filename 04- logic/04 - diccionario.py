import os
os.system("cls")

###
# Diccionarios son colecciones de pares tipo clave | valor.
# Permiten almacenar datos relacionados
###

# Ejemplo típico de diccionario
diccionario_1 = {
    "es_mayor_de_edad": True,
    "tiene_hijos": True,
    "lista": [1, 2, 3, 4],
    "nombre_apellido": {
        "nombre": "Raúl",
        "apellido": "gomez"
    },
    "socials": {
        "twitter": "@cian161",
        "instagram": "@thiago__161",
        "facebook": "Thiago Peire"
    },
    "numero_telefonico": 28044235365
}

# Para acceder y printar a los valores
print(diccionario_1["tiene_hijos"])
print(diccionario_1["socials"]["facebook"])
print(diccionario_1["lista"][2])

# Cambiar valores y printarlo
diccionario_1["lista"][2] = 10
print(diccionario_1["lista"])  # Cambia el valor de la posicion 2, por 10

# Para eliminar completamente una propiedad
del diccionario_1["tiene_hijos"]
print("\n", diccionario_1)

# Elimina el elemento del diccionario, pero devuelve el valor en una variable
es_mayor_de_edad = diccionario_1.pop("es_mayor_de_edad")
print(f"Es mayor de edad: {es_mayor_de_edad}")

# Update
# Sobreescribir un diccionario por otro diccionario

a = {"edad": 25, "nombre": "Thiago", "es_mayor": True}
b = {"edad": 30, "nombre": "Juan", "tiene_licencia": False}

print("\n", a,"\n", b)

a.update(b) #Actualiza los datos de a por los de b. Si hay elementos que no existen en a de b, se agregan.

print(a)
# Resultado:  {'edad': 30, 'nombre': 'Juan', 'es_mayor': True, 'tiene_licencia': False}

#Comprobar si existe una propiedad
print("\nComprobar la existencia  de una propiedad")
print("name" in diccionario_1) #False
print("lista" in diccionario_1) #True

#Para obtener todas las keys:
print("\nclaves: ")
print(diccionario_1.keys())
#Obtener todos los valores:
print("\nValores: ")
print(diccionario_1.values())
print()
print(diccionario_1.values())
#obtener las keys y el valor:
print("\nitems: ")
print(diccionario_1.items())
print()
#Muy util para un for donde querramos guardar 
for key,value in diccionario_1.items():
    print("llave:",key,"| valor:",value)