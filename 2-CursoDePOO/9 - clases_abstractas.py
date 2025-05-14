from abc import ABC, abstractmethod

class Persona(ABC):
    @classmethod
    @abstractmethod
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    @classmethod      
    @abstractmethod   # classmethod seguido de un abstractmethod obliga a las clases hijas implementar el metodo "tirar_cv" en este caso.
    def tirar_cv(self):
        pass
    
    @classmethod    #classmethod solo 
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y mi DNI es {self.dni}.")
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, dni, puesto):
        super().__init__(nombre, edad, dni)
        self.puesto = puesto
    
    def tirar_cv(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y mi DNI es {self.dni}. Estoy trabajando como {self.puesto}.")

class Artista(Persona):
    def __init__(self, nombre, edad, dni, habilidad):
        super().__init__(nombre, edad, dni)
        self.habilidad = habilidad
    def tirar_cv(self):
         print(f"Soy {self.nombre}, tengo {self.edad} años y mi DNI es {self.dni}. Soy un artista de {self.habilidad}.")
        
fito = Artista("Fito", 30, "12345678", "música")
fito.tirar_cv()
bostero = Trabajador("Bostero", 40, "87654321", "carpintero")
bostero.tirar_cv()
# En este ejemplo, la clase Persona es una clase abstracta que define un contrato para las clases Trabajador y Artista.