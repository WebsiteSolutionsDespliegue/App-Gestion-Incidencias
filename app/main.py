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
    tecnico: Optional[str] = None


# Datos ficticios cargados en memoria
db_incidencias: List[Incidencia] = [
    Incidencia(
        id=1,
        titulo="Fallo en la impresora",
        descripcion="La impresora de la planta 2 no saca papel",
        estado="Abierta",
        prioridad="Media",
        tecnico="Carlos",
    ),
    Incidencia(
        id=2,
        titulo="Error de login",
        descripcion="Varios usuarios no pueden acceder al portal",
        estado="En proceso",
        prioridad="Alta",
        tecnico="Lucía",
    ),
]


# 3. Endpoint GET /incidencias
@app.get(
    "/incidencias",
    response_model=List[Incidencia],
    status_code=status.HTTP_200_OK,
    summary="Listar todas las incidencias",
)
