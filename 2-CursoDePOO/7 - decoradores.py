# Decoradores en Python
# Un decorador es una funcion que recibe otra funcion como argumento y devuelve una nueva funcion que generalmente 
# extiende el comportamiento de la funcion original antes o despues de ejecutarla.
def decorador(funcion):
    def funcion_decorada():
        print("Antes de la funcion")
        funcion()
        print("Despues de la funcion")
    return funcion_decorada
    
# def saludo():
#     print("hola mundo")  --------> forma menos recomendada de usar decoradores

# saludos = decorador(saludo)
# saludos()

@decorador
def saludo():
    print("hola mundo")
saludo()