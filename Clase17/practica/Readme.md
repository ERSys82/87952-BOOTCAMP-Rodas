# Estructura del proyecto

/
|-- api.py
|-- models/
|   `-- persona.py
|-- repositories/
|   `-- persona_repository.py
`-- services/
    `-- persona_service.py

La API conecta `PersonaService` con el repositorio y arranca la aplicacion.
Para ejecutar el servidor, usa `python api.py` desde esta carpeta.
