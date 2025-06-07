#
# Crie um programa que leia o arquivo de textos numeros.txt, calcule o 
# percentual de valores menores que 5 e imprima o resultado na tela.
#

def menor_que_5(valor):
    return valor < 5

arquivo = open('numeros.txt')
conteudo_do_arquivo = arquivo.read().replace("\n","").replace(" ","").strip().split(",")
conteudo_do_arquivo = list(map(float, conteudo_do_arquivo))
arquivo.close()

numeros_menores_que_5 = len(list(filter(menor_que_5, conteudo_do_arquivo)))
numero_total = len(conteudo_do_arquivo)

percentual = (numeros_menores_que_5 / numero_total) * 100

print(f"O percentual de valores menores que 5 é: {round(percentual,2)}%")
