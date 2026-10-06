from flask import Flask, jsonify, request

from repositories.persona_repository import RepositorioPersona
from services.persona_service import PersonaDuplicadaError, PersonaService


def crear_app(servicio: PersonaService | None = None) -> Flask:
    if servicio is None:
        servicio = PersonaService(RepositorioPersona())

    app = Flask(__name__)

    @app.get("/persona")
    @app.get("/personas")
    def obtener_personas():
        personas = servicio.listar_personas()

        return jsonify([
            {
                "dni": persona.dni,
                "nombre": persona.nombre
            }
            for persona in personas
        ]), 200

    @app.get("/personas/<dni>")
    def obtener_persona(dni):
        persona = servicio.buscar_por_dni(dni)

        if persona is None:
            return jsonify({
                "error": f"No existe una persona con DNI {dni}"
            }), 404

        return jsonify({
            "dni": persona.dni,
            "nombre": persona.nombre
        }), 200

    @app.post("/persona")
    @app.post("/personas")
    def agregar_persona():
        datos = request.get_json()

        if datos is None:
            return jsonify({
                "error": "Debe enviar datos en formato JSON"
            }), 400

        if "dni" not in datos or "nombre" not in datos:
            return jsonify({
                "error": "Debe proporcionar dni y nombre"
            }), 400

        try:
            persona = servicio.agregar_persona(
                datos["dni"],
                datos["nombre"]
            )
        except PersonaDuplicadaError as error:
            return jsonify({
                "error": str(error)
            }), 409
        except (ValueError, TypeError) as error:
            return jsonify({
                "error": str(error)
            }), 400

        return jsonify({
            "dni": persona.dni,
            "nombre": persona.nombre
        }), 201

    return app


app = crear_app()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
