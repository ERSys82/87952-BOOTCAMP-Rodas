from funciones import sumar


def test_sumar_numeros_positivos():
    assert sumar(2, 3) == 5


def test_sumar_numeros_negativos():
    assert sumar(-2, -3) == -5


def test_sumar_positivo_y_negativo():
    assert sumar(10, -4) == 6


def test_sumar_con_cero():
    assert sumar(5, 0) == 5
    assert sumar(0, 5) == 5


def test_sumar_decimales():
    assert sumar(2.5, 3.5) == 6.0


def test_sumar_ceros():
    assert sumar(0, 0) == 0
