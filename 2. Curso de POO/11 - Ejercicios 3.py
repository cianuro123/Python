# Crear un juego de fusion que pida dos personajes y los fusione para aumentar sus habilidades y crear un nuevo personaje.
import os
if os.system != 0:
    os.system("cls")


class Personaje:
    def __init__(self, name, skill, strenght, armor):
        self.name = name
        self.skill = skill
        self.strenght = strenght
        self.armor = armor

    def __fname(self, fst, snd):
        fst = list(str.lower(fst))
        snd = list(str.lower(snd))
        del fst[2:]
        del snd[2:]
        k = []
        fst = list(map(lambda i: k.extend(i), fst))
        snd = list(map(lambda i: k.extend(i), snd))
        k[0] = str.upper(k[0])
        return ''.join(k)

    def __add__(self, other):
        new_name = self.__fname(self.name, other.name)
        new_armor = ((self.armor + other.armor)//2)**2
        new_strenght = ((self.strenght + other.strenght)//2)**2
        return Personaje(new_name, self.skill, new_armor, new_strenght)

    def __str__(self):
        return f'| {self.name} | \nSpecial Skill: {self.skill} \nFuerza: {self.strenght}💪 \nArmor: {self.armor}🛡️\n'


juancete = Personaje("Juan", "Volar🕊️ ", 3, 5)
dominic = Personaje("Dominic", "Invisibilidad🪞 ", 4, 2)
pedro = Personaje("Pedro", "Ceguera💀 ", 1, 2)
roman = Personaje("Roman", "Robar🐭 ", 1, 6)
fusion = (juancete + dominic)
fusion2 = (roman + pedro)
fusion3 = (dominic + roman)
print(fusion)
print(fusion2)
print(fusion3)
print(roman + roman)
print(fusion + fusion3)


# Ej chatgpt
"""Tenés que:
Crear una clase Mascota con nombre y edad.
Implementar el método __repr__ para que devuelva algo que pueda ser reconstruido con eval().
Crear una lista con varias mascotas.
Imprimir repr() de cada una.
Usar eval() para crear una copia de cada mascota y guardarlas en una nueva lista.
"""


class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Mascota(\"{self.nombre}\", {self.edad})"


lurdes = Mascota("lurdes", 3)
roro = Mascota("roro", 4)
coco = Mascota("coco", 2)
mascotas = [lurdes, roro, coco]
nueva_lista = []
for i in mascotas:
    print(i)
    nueva_lista.append(eval(str(i)))
print(nueva_lista)
