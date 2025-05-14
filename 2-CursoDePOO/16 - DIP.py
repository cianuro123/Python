# 🧲 DIP (Dependency Inversion Principle)
# "Los módulos de alto nivel no deben depender de los de bajo nivel. Ambos deben depender de abstracciones."
# Las abstracciones no deben depender de los detalles, los detalles deben depender de las abstracciones.

# 📌 Traducción simple:
# El código principal (de alto nivel) no debería depender directamente del código específico (de bajo nivel).

# Ambos deberían usar interfaces o clases abstractas como puente.

#Mal Ejemplo: 

class EmailService:
    def enviar_email(self, mensaje):
        print(f"Enviando email: {mensaje}")


# class Notificador: ##----> Obligo a que notificador solo sirva para enviar emails, cuando ésta una clase mas grande.
#     def __init__(self):
#         self.servicio_email = EmailService()  # 🔴 dependencia directa a una clase concreta

#     def notificar(self, mensaje):
#         self.servicio_email.enviar_email(mensaje)
        

##Buen ejemplo:

class ServicioNotificacion:
    def enviar(mensaje):
        raise NotImplementedError


class EmailService(ServicioNotificacion):
    def enviar(mensaje):
        print(f"Enviando email: {mensaje}")


class SMSService(ServicioNotificacion):
    def enviar(mensaje):
        print(f"Enviando SMS: {mensaje}")
        
class FAXService(ServicioNotificacion):
    def enviar(mensaje):
        print(f"Enviando FAX: {mensaje}")


class Notificador:
    def __init__(self, servicio: ServicioNotificacion):
        self.servicio = servicio  # ✅ depende de una abstracción, no de una clase en especifico, acepta modificaciones a largo plazo
        

    def notificar(self, mensaje):
        self.servicio.enviar(mensaje)
    
Notificador(EmailService).notificar("Hola soy thiago")
Notificador(SMSService).notificar("Hola soy thiago")
Notificador(FAXService).notificar("Hola soy thiago")