from datetime import date

from flask import Flask, jsonify, request

from models.alumno import Alumno
from repositories.alumno_repository import RepositorioAlumnos


app = Flask(__name__)

# Un único repositorio en memoria mientras la aplicación está ejecutándose.
repositorio = RepositorioAlumnos()


def alumno_a_dict(alumno: Alumno) -> dict:
    """
    Convierte un objeto Alumno a un diccionario
    que pueda ser serializado a JSON.
    """
    return {
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fecha_nacimiento": alumno.fecha_nacimiento.isoformat()
    }


@app.get("/alumnos")
def obtener_alumnos():
    """
    Retorna todos los alumnos.
    """

    alumnos = repositorio.listar()

    return jsonify([
        alumno_a_dict(alumno)
        for alumno in alumnos
    ]), 200


@app.get("/alumnos/<int:legajo>")
def obtener_alumno(legajo: int):
    """
    Retorna un alumno por legajo.
    """

    alumno = repositorio.buscar_por_legajo(legajo)

    if alumno is None:
        return jsonify({
            "error": "Alumno no encontrado",
            "mensaje": f"No existe un alumno con legajo {legajo}."
        }), 404

    return jsonify(alumno_a_dict(alumno)), 200


@app.post("/alumnos")
def crear_alumno():
    """
    Crea un nuevo alumno.
    """

    datos = request.get_json()

    if datos is None:
        return jsonify({
            "error": "Datos inválidos",
            "mensaje": "El cuerpo de la petición debe contener un JSON."
        }), 400

    campos_obligatorios = [
        "legajo",
        "nombre",
        "apellido",
        "fecha_nacimiento"
    ]

    for campo in campos_obligatorios:
        if campo not in datos:
            return jsonify({
                "error": "Campo obligatorio faltante",
                "mensaje": f"El campo '{campo}' es obligatorio."
            }), 400

    try:
        fecha_nacimiento = date.fromisoformat(
            datos["fecha_nacimiento"]
        )

        alumno = Alumno(
            legajo=datos["legajo"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            fecha_nacimiento=fecha_nacimiento
        )

        repositorio.guardar(alumno)

    except (TypeError, ValueError) as error:
        return jsonify({
            "error": "Datos inválidos",
            "mensaje": str(error)
        }), 400

    return jsonify(alumno_a_dict(alumno)), 201


if __name__ == "__main__":
    app.run(debug=True)