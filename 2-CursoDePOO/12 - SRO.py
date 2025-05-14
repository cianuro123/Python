# 🧱 SRP (Single Responsibility Principle)
# "Una clase debe tener una sola razón para cambiar."

# 📌 Traducción simple:
# Una clase debe hacer una sola cosa. Si hace más, dividila en varias.
from abc import ABC, abstractmethod


class Operaciones(ABC):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.ecuacion = ""
        self.resultado = 0

    @abstractmethod
    # @abstractclassmethod -------> es un error ya que "operar" no necesita un abstractclassmethod, solo abstractmethod
    def operar(self):
        pass


class Sumar(Operaciones):
    def __init__(self, valor1, valor2):
        super().__init__(valor1, valor2)

    def operar(self):
        # self.ecuacion = f"{self.valor1} + {self.valor2}"
        # self.resultado = self.valor1 + self.valor2
        # input(f"F(x)= {self.ecuacion} = {self.resultado}\nEnter para continuar")
        return f"F(x)= {valor1} + {valor2} = ", valor1 + valor2  # ----->
        # Hace que la funcion operar solo se encargue de retornar los valores
        # Haciendo la funcion mas limpia y sencilla


class Restar(Operaciones):
    def __init__(self, valor1, valor2):
        super().__init__(valor1, valor2)

    def operar(self):
        # self.ecuacion = f"{self.valor1} - {self.valor2}"
        # self.resultado = self.valor1 - self.valor2
        # input(f"F(x)= {self.ecuacion} = {self.resultado}\nEnter para continuar")
        return f"F(x)= {valor1} - {valor2} = ", valor1 - valor2


class Mult(Operaciones):
    def __init__(self, valor1, valor2):
        super().__init__(valor1, valor2)

    def operar(self):
        # self.ecuacion = f"{self.valor1} * {self.valor2}"
        # self.resultado = self.valor1 * self.valor2
        # input(f"F(x)= {self.ecuacion} = {self.resultado}\nEnter para continuar")
        return f"F(x)= {valor1} * {valor2} = ", valor1 * valor2


class Raiz(Operaciones):
    def __init__(self, valor1, valor2):
        super().__init__(valor1, valor2)

    def operar(self):
        # self.ecuacion = f"{self.valor2}^√{self.valor1}"
        # self.resultado = self.valor1**(1/self.valor2)
        return f"F(x)= √{valor1} = ", valor1**(1/valor2)


class Div(Operaciones):
    def __init__(self, valor1, valor2):
        super().__init__(valor1, valor2)

    def operar(self):
        # self.ecuacion = f"{self.valor1} / {self.valor2}"
        # self.resultado = self.valor1 / self.valor2
        # input(f"F(x)= {self.ecuacion} = {self.resultado}\nEnter para continuar")
        return f"F(x)= {valor2}/{valor1} = ", valor1/valor2
    

class SumaGauss(Operaciones):
    def __init__(self, valor1, valor2):
        super().__init__(valor1, valor2)
    def operar(self):
        return f"F(x)= ({valor2}/2) * ({valor1}+{valor2}) = ", round((valor2/2)*(valor1+valor2))

op_disponibles = {
    1: Sumar,
    2: Restar,
    3: Mult,
    4: Div,
    5: Raiz,
    6: SumaGauss
    
}
while True:
    operacion = int(input(
        "Escribe el número de la operación:\n1. Sumar\n2. Restar\n3. Mult\n4. Dividir\n5. Raíz Cuadrada\n6. Suma de Gauss\n7. Salir\n--> "))
    if operacion == 7:
        break
    if operacion in op_disponibles:
        valor1 = int(input("-> "))
        # ---- Para darle valor por defecto 2 en raiz.
        valor2 = int(input("-> ")) if operacion != 5 else 2

    clase_op = op_disponibles[operacion]
    instancia = clase_op(valor1, valor2)
    ec, op = instancia.operar()
    print(ec, op)
