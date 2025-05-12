from pyclbr import Class


class Estudiante:
    def __init__(self, nombre, grado, edad):
        self.nombre = nombre
        self.grado = grado
        self.edad = edad
    
    def estudiar(self, lugar):
        print(f"El estudiante {self.nombre} está estudiando en {lugar}.")
    
nombre = input("Escribe el nombre del estudiante: ")
grado = input("Escribe el grado del estudiante: ")
edad = input("Escribe la edad del estudiante: ")
estudiar = Estudiante(nombre, grado, edad)


while True:
    quest = input(f"Escribe si querés mandar a {nombre} a estudiar. S/N: ")
    if quest.lower() == "s":
        lugar = input(f"Escribí donde querés que {nombre} estudie a continuacion: ")
        estudiar.estudiar(lugar)
        break
    else:
        print("No es la respuesta esperada. Reintentando...")
        continue

    

    