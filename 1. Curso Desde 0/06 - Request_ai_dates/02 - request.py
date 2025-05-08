# Como hacer peticiones a APIs con Python con y sin dependencias

# 1. Sin dependencias

import urllib.error
import urllib.request
import json
from os import system
if system != "clear":
    system("cls")
from groq import Groq  # type:ignore
import os
from dotenv import load_dotenv
claves = load_dotenv('env')
OPENAI_KEY=os.getenv("OPENAI_KEY")
API_KEY_GEMINI=os.getenv("API_KEY_GEMINI")
API_KEY_HUGGING_FACE=os.getenv("API_KEY_HUGGING_FACE")
DEEPSEEK_KEY=os.getenv("DEEPSEEK_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# 1 - Sin dependencias (mas dificil de usar)
try:
    api_posts = 'https://jsonplaceholder.typicode.com/todos/1'
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Ha surgido un error: {e.reason}")

# 2 - Con dependencias (requests)
import requests  # type:ignore

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
json_response = response.json()
print(json_response[0])

# 3 - Un POST
print("\nPOST:")
api_posts = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.post(api_posts,
                             json={
                                 "title": "capomaster",
                                 "body": "cloroformo",
                                 "userId": 3
                             })
    print(response.json())
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Ocurrio un error: {e}")

# 4 - Un PUT # Actualizar un recurso en este caso el id 1
print("\nPUT:")
api_posts = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.put(api_posts,
                            json={
                                "title": "capomaster",
                                "body": "cloroformo",
                                "userId": 1
                            })
    print(response.json())
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Ocurrio un error: {e}")

import requests
import json
# La diferencia entre PUT y PATCH es que PUT reemplaza el recurso completo, mientras que PATCH solo actualiza los campos especificados.
def call_openaiGPT(api_key,prompt):
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        data={
            "model":"o1-mini",
            "messages":[{
                "role":"user",
                "content":prompt
            }]
        }
        response =requests.post(url, json=data ,headers=headers )
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ocurrio un error: {e}")
api_response=call_openaiGPT(OPENAI_KEY, "Escribe de forma sencilla que es una API y para que sirve.")

print(json.dumps(api_response,indent=2))
print(api_response["messages"]["content"])

# Llamar a la API de DEEPSEEK

# import json
# 
# def call_deepseek(api_key,prompt):
#     try:
#         url = "https://api.deepseek.com/chat/completions"
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {api_key}",
#         }
#         data={
#             "title":"Deepseek",
#             "model":"deepseek-chat",
#             "messages":[{
#                 "role":"user",
#                 "content":prompt
#             }]
#         }
#         response =requests.post(url, json=data ,headers=headers )
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Ocurrio un error: {e}")
# api_response=call_deepseek(Deepseek_KEY, "Escribe de forma sencilla que es una API y para que sirve.")

# print(json.dumps(api_response,indent=2))

# Llamar api de claude
client = Groq(api_key=os.environ.get(GROQ_API_KEY),)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "assistant",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explica de forma sencilla que es una API y para que sirve.",
        }
    ],
    model="llama-3.3-70b-versatile",

)

