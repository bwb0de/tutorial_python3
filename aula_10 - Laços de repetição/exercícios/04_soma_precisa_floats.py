#
# Conforme visto em aulas anteriores, a soma de valores do tipo float
# podem implicar erro de precisão. Para um conjunto pequeno de dados
# esses erros podem ser irrelevantes, contudo na medida em que o volume
# de dados aumenta, o acumulo desses erros podem gerar resutados
# indesejáveis.
#
# Crie uma função que realize a soma precisa de uma sequência de floats.
#
# Nessas situações os numros floats costumam ser convertidos em inteiros
# e, ao final da operação, reconvertidos em float.
#
# Compare os resultados da função criada com a função nativa 'sum' usand
# a sequência 'lista_floats'
#


import random
lista_floats = [(random.randint(1, 99999) / 100) for _ in range(2000)]


def somar_floats(lista_floats: list, casas_decimais_significativas=4) -> float:
    resultado = 0
    casas_decimais = casas_decimais_significativas
    for nf in lista_floats:
        ni = int(nf * (10 ** casas_decimais))
        resultado += ni
    return float(resultado / (10 ** casas_decimais))


# Testes
print("\nComparando resultado entre as funções:") 
print("          'sum':", sum(lista_floats))
print(" 'somar_floats':", somar_floats(lista_floats, casas_decimais_significativas=2))
