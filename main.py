from typing import List, Optional
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="API de Gestión de Incidencias")


# 1. Definición del modelo de datos con Pydantic
class Incidencia(BaseModel):
    id: int
    titulo: str
    descripcion: str
    estado: str  # Ej: "Abierta", "En proceso", "Cerrada"
    prioridad: str  # Ej: "Alta", "Media", "Baja"
    tecnico: Optional[str] = None


# 2. Base de datos simulada en memoria (sin credenciales ni datos sensibles)
db_incidencias: List[Incidencia] = [
    Incidencia(
        id=1,
        titulo="Fallo en la red local",
        descripcion="La oficina del segundo piso no tiene conexión a internet",
        estado="Abierta",
        prioridad="Alta",
        tecnico="Carlos Gómez",
    ),
    Incidencia(
        id=2,
        titulo="Actualización de software",
        descripcion="Pendiente instalar la última versión del sistema operativo en el servidor principal",
        estado="En proceso",
        prioridad="Media",
        tecnico="Laura Martínez",
    ),
]

# 3. Endpoint GET /incidencias
@app.get(
    "/incidencias",
    response_model=List[Incidencia],
    status_code=status.HTTP_200_OK,
    summary="Listar todas las incidencias",
)
