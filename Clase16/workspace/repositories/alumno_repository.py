from datetime import date

from models.alumno import Alumno


class RepositorioAlumnos:
    """
    Repositorio de alumnos persistido en memoria.

    Responsabilidades:
    - almacenar alumnos
    - buscar alumnos por legajo
    - listar alumnos
    - agregar alumnos
    - eliminar alumnos

    Esta implementación usa una lista en memoria.
    """

    def __init__(self) -> None:
        self.__alumnos: list[Alumno] = []
        self.__cargar_datos_iniciales()

    def __cargar_datos_iniciales(self) -> None:
        """
        Carga alumnos de prueba al iniciar el repositorio.
        """

        alumnos_iniciales = [
            Alumno(
                legajo=1,
                nombre="Juan",
                apellido="Perez",
                fecha_nacimiento=date(2000, 5, 10)
            ),
            Alumno(
                legajo=2,
                nombre="Maria",
                apellido="Gomez",
                fecha_nacimiento=date(2001, 8, 15)
            ),
            Alumno(
                legajo=3,
                nombre="Carlos",
                apellido="Lopez",
                fecha_nacimiento=date(1999, 3, 20)
            ),
            Alumno(
                legajo=4,
                nombre="Ana",
                apellido="Martinez",
                fecha_nacimiento=date(2002, 11, 5)
            ),
            Alumno(
                legajo=5,
                nombre="Pedro",
                apellido="Ramirez",
                fecha_nacimiento=date(2000, 1, 30)
            )
        ]

        self.__alumnos.extend(alumnos_iniciales)

    def guardar(self, alumno: Alumno) -> None:
        """
        Guarda un alumno en memoria.

        No permite dos alumnos con el mismo legajo.
        """

        if not isinstance(alumno, Alumno):
            raise TypeError("Solo se pueden guardar objetos de tipo Alumno.")

        if self.buscar_por_legajo(alumno.legajo) is not None:
            raise ValueError(
                f"Ya existe un alumno con el legajo {alumno.legajo}."
            )

        self.__alumnos.append(alumno)

    def buscar_por_legajo(self, legajo: int) -> Alumno | None:
        """
        Busca un alumno por su legajo.

        Retorna:
            Alumno si existe.
            None si no existe.
        """

        for alumno in self.__alumnos:
            if alumno.legajo == legajo:
                return alumno

        return None

    def listar(self) -> list[Alumno]:
        """
        Retorna todos los alumnos almacenados.

        Se devuelve una copia para evitar que desde afuera
        se modifique directamente la lista interna.
        """

        return self.__alumnos.copy()

    def eliminar(self, legajo: int) -> None:
        """
        Elimina un alumno por legajo.
        """

        alumno = self.buscar_por_legajo(legajo)

        if alumno is None:
            raise ValueError(
                f"No existe un alumno con el legajo {legajo}."
            )

        self.__alumnos.remove(alumno)

    def cantidad(self) -> int:
        """
        Retorna la cantidad de alumnos almacenados.
        """

        return len(self.__alumnos)