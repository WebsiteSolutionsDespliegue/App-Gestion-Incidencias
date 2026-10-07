# 2. Endpoint GET /incidencias
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Gestión de Incidencias")


# Modelo de datos de la incidencia
class Incidencia(BaseModel):
    id: int
    titulo: str
    descripcion: str
    estado: str
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

# PUT /incidencias/{id}: Modificar una incidencia existente
@app.put("/incidencias/{id}", response_model=Incidencia)
def editar_incidencia(id: int, incidencia_actualizada: Incidencia):
    for index, inc in enumerate(incidencias_db):
        if inc.id == id:
            incidencias_db[index] = incidencia_actualizada
            return incidencia_actualizada
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Incidencia no encontrada"
    )

# DELETE /incidencias/{id}: Eliminar una incidencia
@app.delete("/incidencias/{id}", status_code=status.HTTP_200_OK)
def eliminar_incidencia(id: int):
    for index, inc in enumerate(incidencias_db):
        if inc.id == id:
            incidencias_db.pop(index)
            return {"mensaje": f"Incidencia con ID {id} eliminada correctamente"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Incidencia no encontrada"
    )
