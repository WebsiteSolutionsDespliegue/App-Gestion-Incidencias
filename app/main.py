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


# Endpoint: Consulta de incidencia por ID
@app.get(
    "/incidencias/{id}",
    response_model=Incidencia,
    status_code=status.HTTP_200_OK,
    summary="Consultar incidencia por ID",
)
def obtener_incidencia_por_id(id: int):
    """Permite consultar los datos de una incidencia concreta a partir de su ID."""
    for incidencia in db_incidencias:
        if incidencia.id == id:
            return incidencia

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se encontró ninguna incidencia con el ID {id}.",
    )
