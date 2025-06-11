#
# Escreva um script que leia o arquivo 'pessoas.txt' e calcule a média de altura das pessoas.
#
# Em seguida apresente um relatório informando:
#    - a quantidade de pessoas na lista
#    - a média da altura (apresentar apenas com duas casas decimais)
#    - a quantidade de pesoas com altura abaixo da média
#    - a quantidade de pessoas com altura acima da média
#


arquivo = open('pessoas.txt')
conteudo = arquivo.read().split(';')
conteudo = list(map(lambda x: x.strip(), filter(None, conteudo)))

def somar_floats(lista_floats: list, casas_decimais_significativas=4) -> float:
    resultado = 0
    casas_decimais = casas_decimais_significativas
    for nf in lista_floats:
        ni = int(nf * (10 ** casas_decimais))
        resultado += ni
    return float(resultado / (10 ** casas_decimais))


alturas = []
qtd_pessoas = 0

for i, linha in enumerate(conteudo[:]):
    qtd_pessoas += 1
    nome, altura, peso = linha.split(',')
    nome, altura, peso = nome.strip(), float(altura), int(peso)
    alturas.append(altura)
    conteudo[i] = nome, altura, peso

soma_alturas = somar_floats(alturas)
media_alturas = sum(alturas) / qtd_pessoas

n_menor_ma = 0
n_maior_ma = 0

for linha in conteudo:
    altura = linha[1]
    if altura < media_alturas:
        n_menor_ma += 1
    elif altura > media_alturas:
        n_maior_ma += 1

print("Relatório:")
print("  - total pessoas:", qtd_pessoas)
print("  - media altura [m]:", f"{media_alturas:.2f}")
print("  - n pessoas menor média:", n_menor_ma)
print("  - n pessoas maior média:", n_maior_ma)
