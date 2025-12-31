# 
# Crie um programa que leia o arquivo 'cidades.txt' e informe a 
# quantidade de cidades listadas. Ordene os registros alfabeticamente 
# e apresente os quatro primeiros registros, cada um em uma linha.
#

arquivo = open('cidades.txt')
conteudo_do_arquivo = arquivo.read().strip().split("; ")
conteudo_do_arquivo.sort()
arquivo.close()

print("Número de cidades listadas:", len(conteudo_do_arquivo))
print("Quatro primeiros registros:", *conteudo_do_arquivo[:4], sep='\n')
