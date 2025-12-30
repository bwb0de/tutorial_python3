#
# Crie a função média aritmética de forma procedural.
#

def media_aritmetica(sequencia: list) -> float:
    soma = 0.0
    n = 0
    for v in sequencia:
        n += 1
        soma += v
    return soma / n
