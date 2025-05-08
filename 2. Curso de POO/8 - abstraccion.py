# Refiere a poder ocultar los detalles complejos de una clase o metodo al desarrollador o al usuario, mostrando 
# solo lo necesario. Esto permite que el usuario no tenga que preocuparse por los detalles internos de la clase o metodo. 

class Auto:
    def __init__(self):
        self.__estado = "apagado"
        
    def encender(self):
        self.__estado = "encendido"
        print("El auto está encendido.")
        
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("El auto está en movimiento.")
        
    def apagar(self):
        self.__estado = "apagado"
        print("El auto fue apagado.")
    
# Esto es un ejemplo de abstraccion, ya que la clase Auto oculta los detalles del funcionamiento interno (como el estado)
# y solo expone los metodos necesarios para interactuar con el objeto (encender, conducir y apagar).
mi_auto = Auto()
mi_auto.conducir()
mi_auto.apagar()
mi_auto.conducir()