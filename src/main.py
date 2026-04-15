from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware

# enuns dos sexo dos animais haha sexo kkk 
class sexoEnum(str, Enum):
    macho = "macho"
    femea = "femẽa"

# classe principal do cadastro dos animais herdando basemodel
class Animal(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    nome : str
    idade: int
    sexo : sexoEnum
    cor : str

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# animais ficam armazenados nesta lista
db_animais = []

# cadastrar animais
@app.post("/animais/")
async def cadastrar_animal(animal:Animal):
    animal.id = uuid4()
    db_animais.append(animal)
    return animal


# retornar todos os animais
@app.get("/animais/consulta/")
async def consultar_animais():
    return db_animais

# retornar animal com o parametro id
@app.get("/animais/id/{id}")
async def consultar_animal_id(id : UUID):
    for animal in db_animais:
        if animal.id == id:
            return animal
    return{"erro" : "animal não encontrado"}

# deletar animal
@app.delete("/animais/deletar/{id}")
async def deletar_animal(id : UUID):
    for animal in db_animais:
        if animal.id == id:
            db_animais.remove(animal)
            return{"message" : "Animal deletado com sucesso"}
        
    return{"message" : "Animal não encontrado"}




    

    
