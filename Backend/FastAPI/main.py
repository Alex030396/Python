from fastapi import FastAPI

app = FastAPI()

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