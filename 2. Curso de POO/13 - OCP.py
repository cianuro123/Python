#Open/Closed Principle
#El OCP (Open/Closed Principle) dice que:

# "El código debe estar abierto a la extensión, pero cerrado a la modificación."

# 🧠 Traducción sencilla:
# Puedes agregar nueva funcionalidad sin tener que cambiar el código ya existente.

# 🛠️ Se logra usando herencia, clases abstractas o interfaces.

class User:
    def __init__(self, nombre, email, tel):
        self.nombre=nombre
        self.email=email
        self.tel=tel
        
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def Notificar(self):
        raise NotImplementedError #----> Obliga a que todas las clases hijas deban implementar este metodo, como usando abstractmethod

class NotifEmail(Notificador):
    def __init__(self, usuario,mensaje):
        super().__init__(usuario, mensaje)
    
    def Notificar(self):
        return f"A {self.usuario.nombre} le llego un email a {self.usuario.email}: {self.mensaje}"
    

class NotifSMS(Notificador):
    def __init__(self, usuario,mensaje):
        super().__init__(usuario, mensaje)
    
    def Notificar(self):
        return f"A {self.usuario.nombre} le llego un email a {self.usuario.tel}: {self.mensaje}"
    
class NotifWapp(Notificador):
    def __init__(self, usuario,mensaje):
        super().__init__(usuario, mensaje)
    
    def Notificar(self):
        return f"A {self.usuario.nombre} le llego un whatsapp a {self.usuario.tel}: {self.mensaje}"
    
usuario1 = User("Juan", "juangay2005@gmail.com", 2805435903)

print(NotifEmail(usuario1, "Juan, eres tan gay k das asko HAHAHAHAHAH").Notificar())
