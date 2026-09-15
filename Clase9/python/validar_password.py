def validar_password(password):
    if not isinstance(password, str):
        return {
            "valid": False,
            "message": "La contraseña debe ser un texto."
        }

    if " " in password:
        return {
            "valid": False,
            "message": "La contraseña no debe contener espacios."
        }

    if len(password) < 10:
        return {
            "valid": False,
            "message": "La contraseña debe tener al menos 10 caracteres."
        }

    if len(password) > 20:
        return {
            "valid": False,
            "message": "La contraseña no debe superar los 20 caracteres."
        }

    if not any(caracter.isdigit() for caracter in password):
        return {
            "valid": False,
            "message": "La contraseña debe contener al menos un número."
        }

    if not any(caracter.isalpha() for caracter in password):
        return {
            "valid": False,
            "message": "La contraseña debe contener al menos una letra."
        }

    if not any(caracter.isupper() for caracter in password):
        return {
            "valid": False,
            "message": "La contraseña debe contener al menos una letra mayúscula."
        }

    if not any(caracter.islower() for caracter in password):
        return {
            "valid": False,
            "message": "La contraseña debe contener al menos una letra minúscula."
        }

    if not any(not caracter.isalnum() for caracter in password):
        return {
            "valid": False,
            "message": "La contraseña debe contener al menos un símbolo especial."
        }

    return {
        "valid": True,
        "message": "La contraseña es válida."
    }