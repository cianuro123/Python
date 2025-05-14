# LSP
# 🧩 Liskov Substitution Principle (LSP)
# "Los objetos de una clase hija deben poder usarse en lugar de objetos de la clase padre sin alterar el funcionamiento del programa."

# 📌 Traducción simple:
# Una subclase debe comportarse como su clase base, sin romper el programa si se la reemplaza.

#Mal Ejemplo:

# class Ave:
#     def volar():
#         print("Estoy volando!")


# class Pinguino(Ave):
#     def volar():
#         print("No puedo volar!")
        
# Pinguino.volar()


#Buen Ejemplo

class Ave:
    def mover_alas():
        print("Muevo las alas")    
    


class AveVoladora(Ave):
    def volar():
        print("Puedo volar")
        

class AveNoVoladora(Ave):
    def volar():
        print("No puedo volar")


pinguino = AveNoVoladora.volar()
pinguino = AveVoladora.volar()
Ave.mover_alas()  