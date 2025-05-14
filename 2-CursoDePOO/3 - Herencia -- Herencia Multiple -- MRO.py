# ## La herencia refiere a la capacidad de las clases de heredar propiedades de sus clases padre, ahorrando lineas de codigo
# ## y haciendo mas legible su lectura

class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
class Persona_Con_Capacidades_Diferentes(Persona):
    def __init__(self, edad, nombre, discapacidad):
        super().__init__(edad, nombre) #Cuando se usa el super() no se necesita aclarar el "self"
        self.discapacidad = discapacidad
    def Pequeño_Accidente(self):
        print(f"""ULTIMO MOMENTO: El enfermito {self.nombre} fue hallado desmembrado luego de un brutal atropello producto de un subte en la linea 69. 
                El afectado sufría de {self.discapacidad} y claramente se lo buscó. Tenia {self.edad} años de edad y debido a su discapacidad, su muerte
                estaba destinada tarde o temprano. Un saludito a la familia del atrofiadito.""")
juancito = Persona_Con_Capacidades_Diferentes(20,"Juancito","Autismo")
juancito.Pequeño_Accidente()

class Empleado:
    def __init__(self, empresa):
        self.empresa = empresa
        
class Artista:
    def __init__(self, habilidad, experiencia):
        self.habilidad = habilidad
        self.experiencia = experiencia

#Herencia Multiple
#Las herencias multiples permiten a una clase heredar propiedades de otras clases.
class EmpleadoArtista(Empleado, Artista,Persona):
    def __init__(self, empresa, habilidad, experiencia,edad, nombre, salario):
      Empleado.__init__(self, empresa) #Ahora, al no usar super sino acl
      Artista.__init__(self, habilidad, experiencia)
      Persona.__init__(self, edad, nombre)
      self.salario = salario
    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años. Mi principal habilidad artística es {self.habilidad}. Trabajo en {self.empresa} teniendo ya {self.experiencia} años en la industria, donde cobro actualmente ₽{self.salario} rublos")
        
roberto= EmpleadoArtista(edad = 21, nombre = "Roberto", empresa="Flux", habilidad="correr", experiencia=2, salario="4.000.000")
roberto.presentarse()

## MRO: Es el orden por defecto de python para ejecutar funciones hijas.
#ejemplo:
class A():
    def mostrarse(self):
        print("Esto es A")
        
class B():
    def mostrarse(self):
        print("Esto es B")
        
class C(B):
    pass

class D(C,B):
    pass

class F(D,A):
    pass

obj1 = D()
obj1.mostrarse()
obj2 = F()
obj2.mostrarse()

print(F.mro()) #Muestra directamente el orden de ejecucion de la clase.
print(D.mro())




