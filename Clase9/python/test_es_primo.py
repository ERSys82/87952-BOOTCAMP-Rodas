import es_primo
#Ctrl+i sirve para abrir el promt de la IA, seleccionamos el codigo para poder hacer la consutal con la IA#
#Separar en casos
#Genera tests para numerar que 
#no es primo devuleve false 
#un par de numeros primos devulven true
#si le pasas un string como parametro devuleve false

def test_numero_primo():

    assert es_primo.es_primo(2) is True
    assert es_primo.es_primo(3) is True
    assert es_primo.es_primo(5) is True


def test_numero_no_primo():

    assert es_primo.es_primo(4) is False
    assert es_primo.es_primo(1) is False


def test_string_no_primo():

    assert es_primo.es_primo("string") is False