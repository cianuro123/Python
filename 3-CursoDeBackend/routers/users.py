from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

#! Inicia Servidor: uvicorn users:router --reload
router = APIRouter(prefix="/user",
                tags=["Users"])




class User(BaseModel):  # ? Entidad Usuarios
    # ?-> BaseModel hace que una clase sea interpretada como un json modificable
    id: int
    name: str
    surname: str
    age: int
    url: str


# * Forma correcta: Utiliza la clase User para hacer una lista de usuarios
global users_list
users_list = [User(id=0, name="Juan", surname="Gay", age=20, url="juangay.com"),
              User(id=1, name="Leo", surname="Maricon",
                   age=21, url="www.leomaricon.com"),
              User(id=2, name="Conra", surname="Loli", age=19, url="www.conraloli.com")]


# ** Mostrar la lista|>
@router.get("/all") #! -> Pibe al sv todos los usuarios
async def users():
    return users_list


# ** Mostrar usuarios individuales (Path & Query)
# ? Path. Generalmente utilizado para obtener un recurso fijo y Obligatorio
@router.get("/{id}") #! -> 'get' Pide al servidor un usuario segun su id
async def user(id: int):  # !-> Muestra un usuario con Path
    if type(search_user(id)) == User:
        if type(search_user(id)) == User:
            return search_user(id)
    raise HTTPException(status_code=404, detail="El usuario no existe")


@router.get("/")
async def userqy(id: int):  # !-> Muestra un usuario con Querys
    if usuario_existe(id) is not None:
        return search_user(id)
    raise HTTPException(status_code=404, detail="El usuario no existe")
# ? http://127.0.0.1:8000/user/?id=0
# ? Querys. Generalmente utilizado para obtener un recurso variable y Secundario
# ? Luego del '?' ponemos el parametro de interes igualado al valor buscado


@router.post("/", status_code=201)  # !-> 'post' Crea un usuario
async def usercreate(user: User):
    if (usuario_existe(user.id) is None) or users_list == []:
        users_list.append(user)
        return {"notice": "Usuario creado exitosamente"}
    raise HTTPException(
        status_code=400, detail="El usuario ya se encuentra en la lista")


# **  Eliminar el usuario1|>
@router.delete("/{id}", status_code=202, description="Se pudo")# !-> 'delete' Elimina todo el usuario
async def userdelete(id: int):
    if usuario_existe(id) is not None:
        user = search_user(id)
        users_list.remove(user)
        return {"Notice": "Usuario borrado exitosamente"}
    raise HTTPException(status_code=400, detail="El usuario no existe")


# ** Actualizar el usuario|>
@router.put("/", status_code=202)  # !-> 'put' Actualiza todo el usuario
async def userupdate(user: User):
    if usuario_existe(user.id) is not None:
        for idx, usuario in enumerate(users_list):
            if usuario.id == user.id:
                users_list[idx] = user
        return {"Notice": "Usuario actualizado con exito"}, user
    raise HTTPException(status_code=404, detail="El usuario no existe")


# ¡*Funciones Utilitarias|>
def search_user(id): #? Busca un usuario por id en la base de datos y lo devuelve como lista
    # Filter devuelve unicamente las listas que hagan que la funcion lambda sea True
    users = filter(lambda user: user.id == id, users_list)
    try:
        # -> retorna la primer aparicion del id solicitado.
        return list(users)[0]
    except:
        return "Error: Usuario no encontrado"

def usuario_existe(id): #?Verifica si existe un usuario (user si existe/None si no)
    user = search_user(id)
    return user if isinstance(user, User) else None
