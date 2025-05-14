from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import random

tokens=["asldkmkioangjksñ ANFjkoln off","jashnfdijuadhnfuioasfjnmjiouanfiuonasodmoaski","jsahfdihnafojinmsdoansjdfocnasodmnsaodm","alksjdfiojasnfoisajnmofdimsaoidkmadm,a.","aksjdoisjnfoieamjfoisamdaioksmfiosmad,asd.sad","kloqasjd0omng`fio,a'o+pasd,omfn àosm,fda"]
global usuario_token
usuario_token={}
app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    fullname: str
    email:str
    disabled:bool

class UserDB(User):
    password:str
    

users_db={"thiago":{"username": "thiago",
    "fullname": "Thiago Pro Gamer",
    "email":"thiagopro@yahoo.net",
    "disabled":False,
    "password":"thiagopro666XXX"
    },
    "thiago2":{"username": "thiago2",
    "fullname": "Thiago Pro Gamer XXX",
    "email":"thiagopros@yahoo.net",
    "disabled":True,
    "password":"thiagopro666XXX"
    },
    "thiago3":{"username": "thiago3",
    "fullname": "Thiago XXX Gamer",
    "email":"thiagosi@yahoo.net",
    "disabled":True,
    "password":"thiagopro666"
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token:str = Depends(oauth2)):
        if token not in usuario_token.values():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="Credenciales de autenticacion invalidas",
                                headers={"www-Authenticate":"Bearer"}
                                )
        for usser, tokken in enumerate(usuario_token):
            if token == tokken:
                user=User(**users_db[usser])
                if user.disabled:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                        detail="Usuario inactivo")
                return user

@app.post("/login", status_code=201)
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña Incorrecta")
    
    token = random.choice(tokens)
    global usuario_token
    usuario_token.update({user.username:token})
    return {"access_token":token , "token_type":"bearer"}

@app.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user

#Encontrar por que me dice 500 internal server error