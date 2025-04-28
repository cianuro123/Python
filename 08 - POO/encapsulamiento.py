class Miclase:
    def __init__ (self):
        self.__atributo_privado = "Hola soy un atributo privado"
    def __metodo_privado(self):
        print("hola soy un metodo privado")
    
obj = Miclase()
# print(obj.__atributo_privado) #AttributeError: 'Miclase' object has no attribute '__atributo_privado'
# obj.__metodo_privado() #AttributeError: 'Miclase' object has no attribute '__metodo_privado'

## Getter y Setter

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
        
# obj = Persona("Juan", 23)
# print(obj.get_nombre())
# print(obj.get_edad())

# obj.set_nombre("Roberto")
# print(obj.get_nombre())

# @property es una forma de crear un getter, setter y deleter de una manera mas sencilla y elegante.
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter # ----------> Decorador para el setter. Permite modificar el atributo privado __nombre.
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @edad.deleter # ----------> Decorador para el deleter. Permite eliminar el atributo privado __edad. 
    def edad(self):
        del self.__edad

print("Ejemplo de getter y setter:")
obj = Persona("Juan", 23)
nombre = obj.nombre
print(nombre)
print(obj.edad)
obj.nombre = "Robert"
nombre = obj.nombre
print("Nombre modificado:")
print(nombre)
del obj.edad # Eliminar el atributo edad. Funciona gracias al decorador deleter de lo contrario devuelve un error.
print("Atributo edad eliminado")
# print(obj.edad) # AttributeError: 'Persona' object has no attribute '_Persona__edad'