# 2. Endpoint GET /incidencias
@app.get(
    "/incidencias",
    response_model=List[Incidencia],
    status_code=status.HTTP_200_OK,
    summary="Listar todas las incidencias",
)
def listar_incidencias():
    """Devuelve el listado completo de incidencias registradas en memoria."""
    return db_incidencias
