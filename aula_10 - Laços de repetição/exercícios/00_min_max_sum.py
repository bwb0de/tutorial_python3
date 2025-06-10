#
# Reimplemente as funções min, max e sum de forma procedural.
#

def maximo(sequencia: list) -> float:
    resposta = float("-inf")
    for n in sequencia:
        if n > resposta: resposta = n
    return resposta


def minimo(sequencia: list) -> float:
    resposta = float("inf")
    for n in sequencia:
        if n < resposta: resposta = n
    return resposta


def soma(sequencia: list) -> float
    resposta = 0.0
    for n in sequencia:
        resposta += n
    return resposta
