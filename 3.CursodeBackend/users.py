import fastapi
from pydantic import BaseModel

# Inicia Servidor: uvicorn users:app --reload
app = fastapi.FastAPI()

## Entidad Usuarios
class User(BaseModel): #--------> BaseModel hace que una clase sea interpretada como un json modificable
    id: int
    name: str
    surname: str
    age: int
    url: str    

# Forma incorrecta de mostrar un json de usuarios. Implica mucho trabajo manual
# @app.get("/usersjson")
# async def usersjson():
#     return [{"name":"Juan","surname":"Gay","age":20,"url":"juangay.com"},
#          {"name":"Leo","surname":"Maricon","age":21,"url":"www.leomaricon.com"},
#          {"name":"Conra","surname":"Loli","age":19 ,"url":"www.conraloli.com"}]

# Forma correcta: Utiliza la clase User para hacer una lista de usuarios
users_list = [User(id = 0, name="Juan",surname="Gay",age=20,url="juangay.com"),
         User(id = 1, name="Leo",surname="Maricon",age=21,url="www.leomaricon.com"),
         User(id = 2,name="Conra",surname="Loli",age=19 ,url="www.conraloli.com")]


# Muestra la lista
@app.get("/users")
async def users():
    return users_list

# Filter devuelve unicamente las listas que hagan que la funcion lambda sea True
@app.get("/user/{id}")
async def user(id:int):
    users=filter(lambda user:user.id ==id, users_list)
    return list(users)[0] #--> retorna la primer aparicion del id solicitado.

