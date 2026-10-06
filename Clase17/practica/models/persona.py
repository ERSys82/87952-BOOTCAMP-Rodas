from dataclasses import dataclass, field


@dataclass
class Persona:
    __dni: str = field(repr=False)
    __nombre: str = field(repr=False)

    def __post_init__(self):
        self.__validar_dni(self.__dni)
        self.__validar_nombre(self.__nombre)

    @property
    def dni(self) -> str:
        return self.__dni

    @property
    def nombre(self) -> str:
        return self.__nombre

    def cambiar_nombre(self, nuevo_nombre: str) -> None:
        self.__validar_nombre(nuevo_nombre)
        self.__nombre = nuevo_nombre

    @staticmethod
    def __validar_dni(dni: str) -> None:
        if not isinstance(dni, str):
            raise TypeError("El DNI debe ser una cadena de texto.")

        if not dni.strip():
            raise ValueError("El DNI no puede estar vacío.")

        if not dni.isdigit():
            raise ValueError("El DNI debe contener solamente números.")

    @staticmethod
    def __validar_nombre(nombre: str) -> None:
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")

        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        if len(nombre) > 30:
            raise ValueError(
                "El nombre no puede tener más de 30 caracteres."
            )

        if not nombre.isalpha():
            raise ValueError(
                "El nombre debe contener solamente letras."
            )

        if nombre != nombre.capitalize():
            raise ValueError(
                "El nombre debe comenzar con mayúscula "
                "y las demás letras deben estar en minúscula."
            )