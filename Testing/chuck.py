import requests
import time

while True:
    url = "https://api.chucknorris.io/jokes/random"
    request = requests.get(url)
    data = request.json()
    print(data["value"])
    try:
        print("¿Quieres otro chiste? (s/n)")
        respuesta = input()
        if respuesta.lower() == "s":
            continue
        elif respuesta.lower() == "n":
            print("Gracias por usar el programa")
            time.sleep(1)
            break
        else:
            raise ValueError("Respuesta no válida")
    except ValueError as e:
        print(f"Error: {e} \nPor favor, ingresa 's' o 'n'")
        
