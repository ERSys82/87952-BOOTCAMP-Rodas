# repositories/persona_repository.py

from models.persona import Persona


class RepositorioPersona:

    def __init__(self):
        self.__personas: dict[str, Persona] = {}

        self.__cargar_datos_iniciales()

    def __cargar_datos_iniciales(self) -> None:
        personas_prueba = [
            Persona("1234567", "Eduardo"),
            Persona("2345678", "Carlos"),
            Persona("3456789", "Maria"),
        ]

        for persona in personas_prueba:
            self.__personas[persona.dni] = persona

    def guardar(self, persona: Persona) -> None:
        if persona.dni in self.__personas:
            raise ValueError(
                f"Ya existe una persona con DNI {persona.dni}."
            )

        self.__personas[persona.dni] = persona

    def buscar_por_dni(self, dni: str) -> Persona | None:
        return self.__personas.get(dni)

    def listar(self) -> list[Persona]:
        return list(self.__personas.values())

    def existe_dni(self, dni: str) -> bool:
        return dni in self.__personas