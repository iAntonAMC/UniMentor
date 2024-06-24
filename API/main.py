from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic import EmailStr
from typing import List

import universities_model as universities


# App Instance
app = FastAPI(
    title = "UNIMENTOR-API.v0",
    description = """
    # UNIMENTOR
    ## Sistema de Orientación Universitaria
    API REST para el sistema de orientación universitaria UNIMENTOR
    """,
    version = "0.0",
    terms_of_service = "http://example.com/terms/",
    contact = {
        "name": "iAntonAMC",
        "url":"http://github.com/iAntonAMC",
        "email":"1721110125@utectulancingo.edu.mx",
    },
    license_info = {
        "name":"Apache 2.0",
        "url":"https://www.apache.org/licenses/LICENSE-2.0.html",
    })


# Defining CORS
#TODO: Change the origins to the real domain
origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


# Pydantic Response Models:
class Message(BaseModel):
    message:str



# ROUTES
# Root Route
@app.get("/")
def root():
    return {"message":"Welcome to UNIMENTOR-API.v0"}

# Testeo de la conexión a la base de datos
print(universities.universidades)
