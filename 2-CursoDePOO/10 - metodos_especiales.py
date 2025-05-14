from abc import abstractmethod


class Lista:
    @classmethod
    @abstractmethod
    def __init__(self, dato1, dato2):
        self.dato1 = dato1
        self.dato2 = dato2

    def __str__(self):  # es un metodo especial que se llama cuando se imprime el objeto
        return f"[{self.dato1}, {self.dato2}]"


class Tupla:
    @classmethod
    @abstractmethod 
    def __init__(self, dato1, dato2):
        self.dato1 = dato1
        self.dato2 = dato2

    def __str__(self):
        return f"hola bebe: ({self.dato1}, {self.dato2})"


lista = Lista(["hola si", "123"], 20)
print(lista)  # Salida: [["hola si", "123"], 20]

tupla = Tupla("hola", 20)
print(tupla)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # def __str__(self):
    #     return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def __repr__(self):
        return f'Persona("{self.nombre}","{self.edad}")'


p1 = Persona("juan", 20)

rep = repr(p1)
print(p1)
print(rep)
res = eval(rep)
print(res.nombre)
print(res.edad)


# suma de objetos de clase
class Auto:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __len__(self):
        return len(self.model) + len(self.year)

    def __add__(self, otro):
        nuevo_valor = f"{self.model}, {otro.model}"
        return Auto(nuevo_valor, self.year + otro.year)

    def __str__(self):
        return f"{self.model} {self.year}"


auto1 = Auto("Toyota", 2020)
auto2 = Auto("Honda", 2021)
auto3 = Auto("Mercedes", 2002)
auto4 = Auto("Chevrolet", 2025)
auto5 = Auto("Corolla", 2022)
nuevo_auto = auto1 + auto2 + auto3 + auto4
print((nuevo_auto.model))
