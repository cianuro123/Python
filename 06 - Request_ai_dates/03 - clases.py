# 03 - Las Clases en Python
# Son una forma de encapsular datos y comportamientos en un solo objeto.
# Son plantillas para crear objetos (instancias) que tienen atributos (datos) y métodos (funciones).
import os
if os.system != 0: os.system('cls')
 #Ejemplo basico:
class Coche:
    #  atributo de clase (comparte a todas las instancias)
     tipo = "vehiculo de cuatro ruedas"
    #  metodo especial que es el que construye el objeto
    #  se llama automaticamente este metodo cuando creas la instancia
     def __init__(self, marca, modelo, color):
    #   atributos de la instancia (especificos de cada objeto)
         self.marca=marca
         self.modelo=modelo
         self.color=color

     def arrancar(self):
         print(f"El coche {self.marca} {self.modelo} de color {self.color} arrancó.🚗")

mi_coche = Coche("Toyota", "Corolla", "rojo")


Coche("Ford", "Fiesta", "azul").arrancar()

mi_coche.arrancar()

# clase para llamar a una API de IA (Usando https://huggingface.co/)
import requests
import os
from dotenv import load_dotenv
load_dotenv()  # Carga las variables desde el .env
class CALL_IA:
    def __init__(self, api_key, url):
        self.url = url
        self.api_key = api_key

    def call(self, prompt):
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            }
            data = {
                "inputs": prompt,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(self.url, json=data, headers=headers)
            if response.headers.get("Content-Type") == "application/json":
                return print(response.json())
            else:
                # Si no es json, devolvemos texto plano
                return print(response.text)

        except requests.exceptions.RequestException as e:
            print(f"Ocurrio un error: {e}")
url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
prompt = "hola"
api_key = os.getenv('API_KEY_HUGGING_FACE')
ia_api = CALL_IA(api_key, url)
ia_api.call(prompt)


