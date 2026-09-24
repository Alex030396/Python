from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
# uvicorn users:app --reload



# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1,name="Alex",surname="Briceño",url="https://Ale.com",age=30),
             User(id=2,name="Victoria",surname="Quesada",url="https://VictoriaQuesada.com",age=29),
             User(id=3,name="Luis",surname="Briceno",url="https://LuisBriceno.com",age=35)]

@router.get("/usersjson")
async def usersjson():
    return [{"name":"Alex","surname":"Briceno","url":"https://AlexBriceno.com", "age":30},
            {"name":"Victoria","surname":"Quesada","url":"https://VictoriaQuesada.com", "age":29},
            {"name":"Luis","surname":"Briceno","url":"https://LuisBriceno.com", "age":35}]



# @router.get("/usersclass")
# async def usersclass():
#     return User(name="Alex",surname="Briceño",url="https://Ale.com",age=30)

@router.get("/users")
async def users():
    return users_list


# PATH
@router.get("/users/{id}")
async def user(id: int):
    return search_user(id)
    

# QUERY
@router.get("/user/")
async def user(id: int):
    return search_user(id)
    
@router.post("/user/",response_model=User, status_code = 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user
    
@router.put("/user/")
async def user(user:User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"Error":"No se ha actualizado el usuario"}
    
@router.delete("/user/{id}")
async def user(id:int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"Error":"No se ha eliminado el usuario"}
    




def search_user(id : int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado usuario"}    
    