from funciones import num_mayor


def test_num_mayor_numeros_positivos():
    assert num_mayor([3, 8, 2, 5]) == 8


def test_num_mayor_numeros_negativos():
    assert num_mayor([-7, -2, -10, -4]) == -2


def test_num_mayor_numeros_mixtos():
    assert num_mayor([-5, 0, 12, -1, 7]) == 12


def test_num_mayor_con_numeros_repetidos():
    assert num_mayor([4, 9, 9, 2, 9]) == 9


def test_num_mayor_con_un_elemento():
    assert num_mayor([6]) == 6


def test_num_mayor_con_decimales():
    assert num_mayor([2.5, 7.75, 3.1]) == 7.75

def test_num_mayor_lista_vacia():
    assert num_mayor([]) == None