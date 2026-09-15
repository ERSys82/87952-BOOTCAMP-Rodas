def es_primo(numero):
    if isinstance(numero, bool) or not isinstance(numero, int):
        return False

    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True
