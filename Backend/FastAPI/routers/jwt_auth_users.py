from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"

ACCESS_TOKEN_DURATION = 1

SECRET = "f81d4fae32918bc2891f24d7809923a15b3a4d8c7e12f6904b58e721a9c3b8ef"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str
    
users_db = {
    "Albrix336" : {
        "username": "Albrix336",
        "full_name": "Alex Briceno",
        "email":"albrix336@gmail.com",
        "disabled" : False,
        "password":"$2a$12$9NC0f42ra3d8m.iYVFzVgeOL14NUQ4FoeJg7ThBa6b4bJLDhxAKuq"
    },
    "Albrix337" : {
        "username": "Albrix337",
        "full_name": "Alex Brice7no",
        "email":"albrix337@gmail.com",
        "disabled" : True,
        "password":"$2a$12$sXV091KAnlhuWCy7L5EAROWHOJXiWot2YXc2Btc.6QwsVw5cbkMzS"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticacion invalidas", headers={"WWW-Authenticate":"Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    return search_user(username)
    
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user 

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    access_token = {"sub":user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    return {"access_token":jwt.encode(access_token,SECRET,algorithm=ALGORITHM), "token_type":"bearer"}

@router.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user




# datetime.now(timezone.utc)