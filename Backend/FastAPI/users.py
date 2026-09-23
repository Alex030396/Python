from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
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

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Alex","surname":"Briceno","url":"https://AlexBriceno.com", "age":30},
            {"name":"Victoria","surname":"Quesada","url":"https://VictoriaQuesada.com", "age":29},
            {"name":"Luis","surname":"Briceno","url":"https://LuisBriceno.com", "age":35}]



# @app.get("/usersclass")
# async def usersclass():
#     return User(name="Alex",surname="Briceño",url="https://Ale.com",age=30)

@app.get("/users")
async def users():
    return users_list


# PATH
@app.get("/users/{id}")
async def user(id: int):
    return search_user(id)
    

# QUERY
@app.get("/user/")
async def user(id: int):
    return search_user(id)
    
def search_user(id : int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado usuario"}    