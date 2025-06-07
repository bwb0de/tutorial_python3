#
# Retorne ao código do IMC da aula passada e converta-o em uma função 
# personalizada.
#
# Crie um programa que leia o arquivo pessoas.txt e identifique quantas
# pessoas estão em cada uma das categorias definidas na função IMC.
#
# Dica: usar dicionários, listas, map e shell interativo para depurar...
#

resposta = {
    "Muito abaixo do peso": 0,
    "Abaixo do peso": 0,
    "Peso normal": 0,
    "Acima do peso": 0,
    "Obesidade I": 0,
    "Obesidade II (severa)": 0,
    "Obesidade III (mórbida)": 0
}

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


def avaliar_imc_informacoes(linha_separada, resposta=resposta): 
    peso = float(linha_separada[2])
    altura = float(linha_separada[1])
    imc = calcular_imc(peso, altura)
    classe = classificacao_imc(imc)
    resposta[classe] += 1


arquivo = open('pessoas.txt')
conteudo_do_arquivo = arquivo.read().strip().replace('; ',';').split(';')
conteudo_do_arquivo = tuple(map(separar_informacoes, conteudo_do_arquivo))
arquivo.close()

conteudo_do_arquivo = tuple(map(avaliar_imc_informacoes, conteudo_do_arquivo))
total_pessoas = len(conteudo_do_arquivo)

print("Número de pessoas conforme a categoria")
print(" - Muito abaixo do peso:", resposta["Muito abaixo do peso"])
print(" - Abaixo do peso:", resposta["Abaixo do peso"])
print(" - Peso normal:",  resposta["Peso normal"])
print(" - Acima do peso:", resposta["Acima do peso"])
print(" - Obesidade I:", resposta["Obesidade I"])
print(" - Obesidade II:", resposta["Obesidade II (severa)"])
print(" - Obesidade III:", resposta["Obesidade III (mórbida)"])
print(" # Total de pessoas:", total_pessoas)

