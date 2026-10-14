from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True, init=False)
class Alumno:
    __legajo: int
    __nombre: str
    __apellido: str
    __fecha_nacimiento: date

    def __init__(
        self,
        legajo: int,
        nombre: str,
        apellido: str, 
        fecha_nacimiento: date
    ) -> None:
        self.__validar_legajo(legajo)
        self.__validar_texto(nombre, "nombre")
        self.__validar_texto(apellido, "apellido")
        self.__validar_fecha_nacimiento(fecha_nacimiento)

        object.__setattr__(self, "_Alumno__legajo", legajo)
        object.__setattr__(self, "_Alumno__nombre", nombre) 
        object.__setattr__(self, "_Alumno__apellido", apellido)
        object.__setattr__(self, "_Alumno__fecha_nacimiento", fecha_nacimiento)

    @property
    def legajo(self) -> int:
        return self.__legajo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento

    @staticmethod
    def __validar_legajo(legajo: int) -> None:
        if not isinstance(legajo, int):
            raise TypeError("El legajo debe ser un entero.")

        if legajo <= 0:
            raise ValueError("El legajo debe ser mayor que cero.")

    @staticmethod
    def __validar_texto(valor: str, campo: str) -> None:
        if not isinstance(valor, str):
            raise TypeError(f"El {campo} debe ser un texto.")

        if not valor:
            raise ValueError(f"El {campo} es obligatorio.")

        if " " in valor:
            raise ValueError(f"El {campo} no puede contener espacios.")

        if not valor.isalpha():
            raise ValueError(f"El {campo} no puede contener números ni símbolos.")

        if not valor[0].isupper():
            raise ValueError(f"La primera letra del {campo} debe ser mayúscula.")

    @staticmethod
    def __validar_fecha_nacimiento(fecha_nacimiento: date) -> None:
        if not isinstance(fecha_nacimiento, date):
            raise TypeError("La fecha de nacimiento debe ser un objeto date.")

        if fecha_nacimiento > date.today():
            raise ValueError("La fecha de nacimiento no puede estar en el futuro.")

    def __str__(self) -> str:
        return (
            f"Alumno(legajo={self.__legajo}, nombre='{self.__nombre}', "
            f"apellido='{self.__apellido}', fecha_nacimiento={self.__fecha_nacimiento})"
        )