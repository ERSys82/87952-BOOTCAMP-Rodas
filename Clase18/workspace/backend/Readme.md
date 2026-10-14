
# Estructura del proyecto

/
├── api.py
├── models/
│   └── alumno.py
└── repositories/
    └── alumno_repository.py
├── services/
│   └── alumno_service.py

# CORS

La API permite solicitudes desde cualquier origen (`Access-Control-Allow-Origin: *`)
para sus endpoints `GET` y `POST`, incluyendo las solicitudes preflight `OPTIONS`.
No habilita credenciales.
