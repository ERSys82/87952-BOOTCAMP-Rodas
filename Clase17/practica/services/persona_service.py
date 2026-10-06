# services/persona_service.py

from models.persona import Persona
from repositories.persona_repository import RepositorioPersona


class PersonaDuplicadaError(ValueError):
    pass


class PersonaService:

    def __init__(self, repositorio: RepositorioPersona):
        self.__repositorio = repositorio

    def listar_personas(self) -> list[Persona]:
        return self.__repositorio.listar()

    def buscar_por_dni(self, dni: str) -> Persona | None:
        return self.__repositorio.buscar_por_dni(dni)

    def agregar_persona(self, dni: str, nombre: str) -> Persona:

        if self.__repositorio.existe_dni(dni):
            raise PersonaDuplicadaError(
                f"Ya existe una persona con DNI {dni}."
            )

        persona = Persona(
            dni,
            nombre
        )

        self.__repositorio.guardar(persona)

        return persona