from fastapi import Depends, APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import random

tokens=["asldkmkioangjksñ ANFjkoln off","jashnfdijuadhnfuioasfjnmjiouanfiuonasodmoaski","jsahfdihnafojinmsdoansjdfocnasodmnsaodm","alksjdfiojasnfoisajnmofdimsaoidkmadm,a.","aksjdoisjnfoieamjfoisamdaioksmfiosmad,asd.sad","kloqasjd0omng`fio,a'o+pasd,omfn àosm,fda","wqekfioksdmofiasofmopiasmfoisamfdoisamidjniof","lkasjfiudsaofasoidmnoiasmdosìamdfpuionmf",'3lasdf8sad94f9sd6a2d9jmfdifiojfoikj',"soanfouisn39844895u32498jf9d79432u"]
global usuario_token
usuario_token={}
router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login2")


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
    "disabled":False,
    "password":"thiagopro666XXX"
    },
    "thiago3":{"username": "thiago3",
    "fullname": "Thiago XXX Gamer",
    "email":"thiagosi@yahoo.net",
    "disabled":False,
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
    if token not in usuario_token.keys():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticacion invalidas",
                            headers={"www-Authenticate":"Bearer"})
    
    usuario=usuario_token.get(token)                        
    user = User(**users_db.get(usuario))
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario deshabilitado")
                            
    return user


@router.post("/login2", status_code=201)
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    user = search_user_db(form.username)
    if form.password != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña Incorrecta")
    
    token = random.choice(tokens)
    global usuario_token
    usuario_token.update({token:user.username})
    return {"access_token":token , "token_type":"bearer"}

@router.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user
