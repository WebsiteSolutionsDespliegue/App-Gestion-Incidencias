# Creacion del Security.md
Viendo que tengo que diseñar el archivo puesto que mi rol es de escritura.

# Política de Seguridad (SECURITY.md)

## 1. Reporte de Vulnerabilidades e Incidentes
Si detectas un posible incidente de seguridad o una vulnerabilidad en este proyecto, **no abras un Issue público**. Por favor, comunícate directamente con el equipo de desarrollo enviando un correo electrónico a:
* **Contacto principal:** [jmunpar1307@g.educaand.es]
* **Asunto sugerido:** INCIDENTE SEGURIDAD - [App-Gestion-Incidencias]

## 2. Manejo de Secretos y Credenciales
Para mantener la integridad del proyecto, queda estrictamente prohibido publicar credenciales, contraseñas, tokens de API o cualquier tipo de secreto real en el repositorio.

Recuerda que **ningún secreto real debe aparecer** en:
* Issues o discusiones públicas.
* Pull Requests (PRs).
* Capturas de pantalla adjuntas.
* Historial de commits.

## 3. Uso de Variables de Entorno
Todas las configuraciones sensibles deben gestionarse localmente a través de un archivo `.env`, el cual está excluido del control de versiones mediante el archivo `.gitignore`. Para referencia de configuración, se proporciona exclusivamente el archivo `.env.example` con valores ficticios o de plantilla.

