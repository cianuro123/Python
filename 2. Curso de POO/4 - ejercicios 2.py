##Ej. 1:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def mostrar_grado(self):
        print(f"Mi grado es: {self.grado}º")
        
est = Estudiante("Rafael", 12, 6)
print(est.edad)
print(est.grado)
print(est.nombre)

est.mostrar()
est.mostrar_grado()

########################################
##Ej. 2:

class Animal:
    def comer(self):
        print("Estoy comiendo")
class Mamifero(Animal):
    def __init__(self):
        super().__init__()
    def amamantar(self):
        print("Estoy amamantando")
class Ave(Animal):
    def __init__(self):
        super().__init__()
    def volar(self):
        print("Estoy volando")

class Murcielago(Mamifero,Ave):
    def __init__(self):
        super().__init__()
    def llamar(self):
        self.volar()
        self.amamantar()
        self.comer()
obj = Murcielago()
obj.llamar()
print(Murcielago.mro())