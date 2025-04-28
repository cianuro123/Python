from os import system
if system != 0: system("cls")

class Tazas:
    def __init__(self, tamaño, color, origen, modelo): #Los atributos del objeto
        self.modelo = modelo
        self.tamaño = tamaño
        self.color = color
        self.origen = origen
    def servir(self,liquid): #Las acciones que hace el objeto (Metodos)
        print(f"Estas sirviendo {liquid } desde la taza de {self.modelo}")

# taza1 = Tazas("5cm x 3cm", "rojo", "Vietnam")
taza2 = Tazas("20cm x 40cm", "violeta", "China", "batman")
taza2.servir("té")
