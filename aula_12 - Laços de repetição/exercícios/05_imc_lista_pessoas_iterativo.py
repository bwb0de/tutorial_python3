#
# Reimplemente o programa do IMC substituindo as funções map por laços 
# de repetição.
#


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc,2)
    return imc


def classificacao_imc(imc):
    if imc < 17.00: 
        return "Muito abaixo do peso"
    elif 17.00 <= imc <= 18.49: 
        return "Abaixo do peso"
    elif 18.50 <= imc <= 24.99: 
        return "Peso normal"
    elif 25.00 <= imc <= 29.99: 
        return "Acima do peso"
    elif 30.00 <= imc <= 34.99: 
        return "Obesidade I"
    elif 35.00 <= imc <= 39.99: 
        return "Obesidade II (severa)"
    elif imc >= 40.00: 
        return "Obesidade III (mórbida)"


def separar_informacoes(linha):
    linha_separada = linha.strip().split(",")
    return linha_separada


def avaliar_imc_informacoes(linha_separada): 
    peso = float(linha_separada[2])
    altura = float(linha_separada[1])
    imc = calcular_imc(peso, altura)
    classe = classificacao_imc(imc)
    linha_separada_e_avaliada = (*linha_separada, imc, classe)
    return linha_separada_e_avaliada

def selecionar_grupo_muito_abaixo(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Muito abaixo do peso"

def selecionar_grupo_abaixo(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Abaixo do peso"

def selecionar_grupo_normal(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Peso normal"

def selecionar_grupo_acima(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Acima do peso"

def selecionar_grupo_obesidade1(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Obesidade I"

def selecionar_grupo_obesidade2(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Obesidade II (severa)"

def selecionar_grupo_obesidade3(linha_separada_e_avaliada):
    return linha_separada_e_avaliada[-1] == "Obesidade III (mórbida)"

arquivo = open('pessoas.txt')
conteudo_do_arquivo = arquivo.read().strip().replace('; ',';').split(';')
arquivo.close()

conteudo_do_arquivo_separado = []
for linha in conteudo_do_arquivo:
    linha_separada = separar_informacoes(linha)
    conteudo_do_arquivo_separado.append(linha_separada)
conteudo_do_arquivo = tuple(conteudo_do_arquivo_separado); del(conteudo_do_arquivo_separado)

conteudo_do_arquivo_avaliado = []
for linha_separada in conteudo_do_arquivo:
    linha_avaliada = avaliar_imc_informacoes(linha_separada)
    conteudo_do_arquivo_avaliado.append(linha_avaliada)
conteudo_do_arquivo = tuple(conteudo_do_arquivo_avaliado); del(conteudo_do_arquivo_avaliado)

total_pessoas = len(conteudo_do_arquivo)

print("Número de pessoas conforme a categoria")
print(" - Muito abaixo do peso:", len(tuple(filter(selecionar_grupo_muito_abaixo, conteudo_do_arquivo))))
print(" - Abaixo do peso:", len(tuple(filter(selecionar_grupo_abaixo, conteudo_do_arquivo))))
print(" - Peso normal:", len(tuple(filter(selecionar_grupo_normal, conteudo_do_arquivo))))
print(" - Acima do peso:", len(tuple(filter(selecionar_grupo_acima, conteudo_do_arquivo))))
print(" - Obesidade I:", len(tuple(filter(selecionar_grupo_obesidade1, conteudo_do_arquivo))))
print(" - Obesidade II:", len(tuple(filter(selecionar_grupo_obesidade2, conteudo_do_arquivo))))
print(" - Obesidade III:", len(tuple(filter(selecionar_grupo_obesidade3, conteudo_do_arquivo))))
print(" # Total de pessoas:", total_pessoas)


