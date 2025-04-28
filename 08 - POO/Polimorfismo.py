# El polimorfismo es una propiedad de los objetos de contar con varias "formas" de funcionar. Por ejemplo, las variables
# son polimorfas ya que cualquier variable puede tener cualquier valor y seguir funcionando

class Perro:
    def sonido():
        return "Guau"
class Gato:
    def sonido():
        return "Miau"
class Vaca:
    def sonido():
        return "Mu"

print(Perro.sonido()) 
print(Gato.sonido())
print(Vaca.sonido())
#Este es un ejemplo de polimorfismo, ya que las tres clases tienen el mismo método "sonido" pero cada una devuelve un valor diferente.
#En este caso, el polimorfismo se logra a través de la definición de un método con el mismo nombre (sonido) en diferentes clases (Perro, Gato, Vaca).
print("\n")
def hacer_sonido(animal):
    return animal.sonido()
print(hacer_sonido(Perro)) #Guau
print(hacer_sonido(Gato)) #Miau
print(hacer_sonido(Vaca)) #Mu
#En este caso tenemos polimorfismo de funcion, ya que la funcion hacer_sonido() puede responder diferente segun el objeto que le pasemos.

#En el ejemplo siguiente se puede ver un polimorfismo de herencia, ya que las clases Perro, Gato y Vaca heredan de la clase Animal y cada una implementa su propio método sonido().
#Esto tambien permite que 

class Animal:
    def sonido(self):
        pass
class Perro(Animal):
    def sonido(self):
        return "Guau"
class Gato(Animal):
    def sonido(self):
        return "Miau"
class Vaca(Animal):
    def sonido(self):
        return "Mu"
    
def hacer_sonido(animal):
    return animal.sonido()
