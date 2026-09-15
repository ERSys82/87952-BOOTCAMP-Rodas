from validar_password import validar_password


def test_password_valida():
    resultado = validar_password("ClaveSegura123!")
    #assert: para verificar si una condición se cumple
    assert resultado["valid"] is True
    assert resultado["message"] == "La contraseña es válida."


def test_password_debe_contener_numeros():
    resultado = validar_password("ClaveSegura!!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña debe contener al menos un número."


def test_password_debe_contener_letras():
    resultado = validar_password("1234567890!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña debe contener al menos una letra."


def test_password_longitud_minima():
    resultado = validar_password("Clave12!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña debe tener al menos 10 caracteres."


def test_password_longitud_maxima():
    resultado = validar_password("ClaveSegura1234567890!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña no debe superar los 20 caracteres."


def test_password_debe_tener_simbolo_especial():
    resultado = validar_password("ClaveSegura123")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña debe contener al menos un símbolo especial."


def test_password_debe_tener_mayuscula():
    resultado = validar_password("clavesegura123!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña debe contener al menos una letra mayúscula."


def test_password_debe_tener_minuscula():
    resultado = validar_password("CLAVESEGURA123!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña debe contener al menos una letra minúscula."


def test_password_no_debe_tener_espacios():
    resultado = validar_password("Clave Segura123!")

    assert resultado["valid"] is False
    assert resultado["message"] == "La contraseña no debe contener espacios."


def test_password_longitud_exacta_minima():
    resultado = validar_password("Clave12!Aa")

    assert resultado["valid"] is True
    assert resultado["message"] == "La contraseña es válida."


def test_password_longitud_exacta_maxima():
    resultado = validar_password("ClaveSegura1234!Abcd")

    assert resultado["valid"] is True
    assert resultado["message"] == "La contraseña es válida."