from fastapi import FastAPI
from routers import products,users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# ROUTERS
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"),name="static")

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/url")
async def url():
    return {"url_curso":"https://AlexBriceno.com/python"}

# Iniciar al server:  uvicorn main:app --reload
# Cerrar el server: Ctrl + C
# Documentacion con Swagger: https://127.0.0.1:8000/docs
# Documentacion con Redocly: https://127.0.0.1:8000/redoc
# Instalar Thunder Client