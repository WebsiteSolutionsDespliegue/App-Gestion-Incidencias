from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de incidencias")

# Modelo de datos del PDF
class Incidencia(BaseModel):
    id: int
    titulo: str
    descripcion: str
    estado: str = "abierta"
    prioridad: str
    tecnico: str

# Base de datos en memoria
incidencias_db: List[Incidencia] = []

@app.get("/")
def inicio():
    return {"mensaje": "API de incidencias operativa"}

# POST /incidencias: Crear nueva incidencia
@app.post("/incidencias", status_code=status.HTTP_201_CREATED, response_model=Incidencia)
def crear_incidencia(incidencia: Incidencia):
    for inc in incidencias_db:
        if inc.id == incidencia.id:
            raise HTTPException(
                status_code=400, 
                detail="Ya existe una incidencia con este ID"
            )
    incidencias_db.append(incidencia)
    return incidencia