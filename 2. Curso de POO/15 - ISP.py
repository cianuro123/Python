# 🎛️ Interface Segregation Principle (ISP)
# "Una clase no debería depender de interfaces que no usa."

# 📌 Traducción simple:
# No obligues a una clase a implementar métodos que no necesita.

#Mal ejemplo:
# class Humano:
#     def comer():
#         print("estoy comiendo")
#     def trabajar():
#         print("estoy trabajando")
#     def dormir():
#         print("estoy durmiendo")


# class Robot(Humano):
#     def trabajar():
#         print("estoy trabajando")

#     def comer():
#         print("Error: los robots no comen")
    
#     def dormir():
#         print("Error: los robots no duermen")
        

#Buen ejemplo:

class Trabajador:
    def trabajar():
        pass

class Dormilon:
    def dormir():
        pass
        
class Comedor:
    def comer():
        pass
        
class Humano(Trabajador, Comedor, Dormilon):
    def comer():
        print("Estoy comiendo")
    
    def dormir():
        print("estoy durmiendo")
        
    def trabajar():
        print("estoy trabajando")

class Robot(Trabajador):
    def trabajar():
        print("estoy trabajando")
        

Robot.trabajar()

Humano.comer()
Humano.dormir()
Humano.trabajar()
