
from fastapi import Depends, APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta



ALGORITHM = "HS256"
ACCES_TOKEN_DURATION= 10 #!este valor es alto para que no de error, datetime.now() no funciona correctamente
SECRET="$2a$12$RffjILLDEZZSiBWHzk7kyeWFFYQ/PJ8TeF7Ccw9vWgtUDcySdK"

router=APIRouter() #* Crea la api del tipo APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):#* Clase usuarios (sin password)
    username: str
    fullname: str
    email:str
    disabled:bool

class UserDB(User):#* Clase usuarios (con password)
    password:str
    

users_db={"thiago1":{"username": "thiago1", #* "Base de datos" de usuarios
    "fullname": "Thiago Pro Gamer",
    "email":"thiagopro@yahoo.net",
    "disabled":False,
    "password":"$2a$12$krueOfMnErq4PiLUeR.U3uqwaAC498q0uAVifg7iheOUjcPaxf/7a"
    },
    "thiago2":{"username": "thiago2",
    "fullname": "Thiago Pro Gamer XXX",
    "email":"thiagopros@yahoo.net",
    "disabled":False,
    "password":"$2a$12$ynXaC0cQIi0BVlE7OD18meL4ynoEGxE2ffg444PKqsq7I0L7g86Va"
    },
    "thiago3":{"username": "thiago3",
    "fullname": "Thiago XXX Gamer",
    "email":"thiagosi@yahoo.net",
    "disabled":True,
    "password":"$2a$12$hUnT6M/.pkrkS.D9Gr69ZubkXdpXIXO2lz4DROWMArle5VVRVQAPS"
    }
}


@router.post("/login", status_code=200)
async def login(form:OAuth2PasswordRequestForm = Depends()):#* Define la operacion Login 
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    user_db = search_user_db(form.username)
        
    is_correct = crypt.verify(form.password, user_db.password)
    
    if not is_correct:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta")
    
    access_token = {
        "sub":user_db.username,
        "exp":datetime.now()+timedelta(hours=ACCES_TOKEN_DURATION)#! datetime.now() no da la hora correcta, está atrasado una hora aprox
    }
    
    
    return {"access_token":jwt.encode(access_token, SECRET, algorithm=ALGORITHM)}

async def auth_user(token:str = Depends(oauth2)): #* Define como verificar y autorizar usuarios
    exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticacion invalidas",
                            headers={"www-Authenticate":"Bearer"})
    
    try:
        username = jwt.decode(token,SECRET, algorithms=ALGORITHM).get("sub")
        if username == None:
            raise exeption

    except JWTError as e:
        raise [exeption, e]
    
    return search_user(username)

async def current_user(user:User = Depends(auth_user)): #*Verifica el estado del usuario (Enabled/Disabled)
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario deshabilitado")
    return user

@router.get("/users/me")
async def me(user:User = Depends(current_user)): #* Define como devolver la info. del usuario
    return user 


def search_user_db(username:str):#* Encontrar por username a un usuario y devolverlo con password
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):#* Encontrar por username a un usuario y devolverlo sin password
    if username in users_db:
        return User(**users_db[username])



    



    